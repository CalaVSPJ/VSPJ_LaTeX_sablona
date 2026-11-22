#!/usr/bin/env python3
"""Fakta z PDF závěrečné práce pro kontrolní skill (JSON na stdout).

Použití:
    python3 vytahni.py PRACE.pdf --souhrn          # přehled všech stran
    python3 vytahni.py PRACE.pdf --strany 3-5,7    # podrobná fakta vybraných stran
    python3 vytahni.py PRACE.pdf --text 10-12      # prostý text stran

Jednotky pt, počátek v levém horním rohu, strany číslované fyzicky od 1.
Pásy inkoustu se měří stejně jako hodnoty v docs/pravidla (288 dpi, šedá, práh 200, mezera 3 px).
"""
from __future__ import annotations

import argparse
import json
import re
import sys

sys.dont_write_bytecode = True

try:
    import pymupdf
except ImportError:  # pragma: no cover - testováno přes subprocess
    pymupdf = None

# Okraje šablony (DOK-F02): text 99,25–523,9 pt vodorovně, 70,9–771,0 pt svisle
HORNI_OKRAJ = 70.9
DOLNI_OKRAJ = 771.0
LEVY_OKRAJ = 99.25
PRAVY_OKRAJ = 523.9
TOLERANCE_OKRAJE = 1.0


def rozsah(spec: str, pocet: int) -> list[int]:
    """„3-5,7“ → [3, 4, 5, 7]; strany mimo 1..pocet → ValueError."""
    cisla: list[int] = []
    for cast in spec.split(","):
        cast = cast.strip()
        if not cast:
            continue
        if "-" in cast:
            od, do = (int(x) for x in cast.split("-", 1))
            if od > do:
                raise ValueError(f"obrácený rozsah stran „{cast}“")
            cisla.extend(range(od, do + 1))
        else:
            cisla.append(int(cast))
    for c in cisla:
        if not 1 <= c <= pocet:
            raise ValueError(f"strana {c} mimo rozsah 1–{pocet}")
    return cisla


def _r(x: float) -> float:
    return round(x, 1)


def pasy_inkoustu(stranka, dpi: int = 288, prah: int = 200, mezera: int = 3) -> list[dict]:
    """Řádky inkoustu na stránce: horní/dolní hrana a vodorovný rozsah v pt."""
    pix = stranka.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY, alpha=False)
    w, h, data = pix.width, pix.height, pix.samples
    k = 72 / dpi
    # bajt < práh → 1, jinak 0 (vyhledávání v C přes bytes.find)
    tab = bytes(1 if b < prah else 0 for b in range(256))
    radky = [min(data[y * w:(y + 1) * w:2]) < prah for y in range(h)]
    pasy = []
    y = 0
    while y < h:
        if radky[y]:
            zacatek = y
            while y < h and (radky[y] or any(radky[y:y + mezera])):
                y += 1
            x0, x1 = w, -1
            for yy in range(zacatek, y, 3):
                maska = data[yy * w:(yy + 1) * w:2].translate(tab)
                prvni = maska.find(1)
                if prvni >= 0:
                    x0 = min(x0, prvni * 2)
                    x1 = max(x1, maska.rfind(1) * 2)
            if x1 >= 0:
                pasy.append({"top": _r(zacatek * k), "bottom": _r(y * k),
                             "x0": _r(x0 * k), "x1": _r(x1 * k)})
        y += 1
    return pasy


def _tesny_bbox(znaky: list[dict]):
    """Rámeček jen z viditelných znaků (bez mezer — Word do rámečku řádku počítá i mezeru na konci)."""
    viditelne = [c["bbox"] for c in znaky if not c["c"].isspace()]
    if not viditelne:
        return None
    return (min(b[0] for b in viditelne), min(b[1] for b in viditelne),
            max(b[2] for b in viditelne), max(b[3] for b in viditelne))


def _radky_textu(stranka) -> list[dict]:
    """Řádky z get_text("rawdict") jako {text, bbox (jen viditelné znaky), spans}."""
    radky = []
    for blok in stranka.get_text("rawdict")["blocks"]:
        for line in blok.get("lines", []):
            spans = []
            for sp in line["spans"]:
                sp = dict(sp, text="".join(c["c"] for c in sp["chars"]))
                tesny = _tesny_bbox(sp["chars"])
                if tesny:
                    sp["bbox"] = tesny
                spans.append(sp)
            text = "".join(sp["text"] for sp in spans).strip()
            bbox = _tesny_bbox([c for sp in line["spans"] for c in sp["chars"]])
            if text and bbox:
                radky.append({"text": text, "bbox": bbox, "spans": spans})
    radky.sort(key=lambda r: (round(r["bbox"][1]), r["bbox"][0]))
    return radky


def _nazev_pisma(nazev: str) -> str:
    return re.sub(r"^[A-Z]{6}\+", "", nazev)


def _vyplnovani(trace: list[dict], span: dict) -> str:
    """Způsob vykreslení úseku z get_texttrace: fill / stroke / fill+stroke (dopočtená tučnost).

    Páruje znaky podle účaří (± 1 pt) a vodorovného rozsahu úseku; fill+stroke, když
    obrysem je vykreslena aspoň polovina vyplněných znaků úseku.
    """
    x0, _, x1, _ = span["bbox"]
    oy = span["origin"][1]
    pocet = {0: 0, 1: 0}
    for t in trace:
        if t["type"] not in pocet:
            continue
        for c in t["chars"]:
            cx, cy = c[2]
            if abs(cy - oy) <= 1 and x0 - 0.5 <= cx <= x1:
                pocet[t["type"]] += 1
    if pocet[1] and pocet[0] and pocet[1] >= pocet[0] / 2:
        return "fill+stroke"
    if pocet[1] and not pocet[0]:
        return "stroke"
    return "fill"


def _usek(span: dict, trace: list[dict]) -> dict:
    pismo = _nazev_pisma(span["font"])
    return {
        "text": span["text"],
        "pismo": pismo,
        "velikost": _r(span["size"]),
        "tucne": bool(span["flags"] & 16) or "bold" in pismo.lower(),
        "kurziva": bool(span["flags"] & 2) or "italic" in pismo.lower(),
        "barva": f"#{span['color']:06x}",
        "vyplnovani": _vyplnovani(trace, span),
    }


def _zahlavi_cislo_prvni(radky: list[dict]):
    zahlavi = [r["text"] for r in radky if r["bbox"][3] < HORNI_OKRAJ]
    zapati = [r["text"] for r in radky if r["bbox"][1] > DOLNI_OKRAJ]
    telo = [r for r in radky if r["bbox"][1] >= 60 and r["bbox"][3] <= DOLNI_OKRAJ
            and not r["bbox"][3] < HORNI_OKRAJ]
    prvni = telo[0] if telo else None
    return (" ".join(zahlavi) or None, " ".join(zapati) or None,
            prvni["text"] if prvni else None, _r(prvni["bbox"][1]) if prvni else None)


def _mimo_okraje(radky: list[dict]) -> list[dict]:
    return [{"text": r["text"], "bbox": [_r(v) for v in r["bbox"]]} for r in radky
            if HORNI_OKRAJ <= r["bbox"][3] and r["bbox"][1] <= DOLNI_OKRAJ
            and (r["bbox"][0] < LEVY_OKRAJ - TOLERANCE_OKRAJE
                 or r["bbox"][2] > PRAVY_OKRAJ + TOLERANCE_OKRAJE)]


def _narovnej(stranka) -> int:
    """Otočenou stránku vrátí (jen v paměti) do nulové rotace, aby souřadnice textu
    a vykreslení souhlasily. Vrací původní rotaci."""
    rotace = stranka.rotation
    if rotace:
        stranka.set_rotation(0)
    return rotace


def souhrn(cesta: str) -> dict:
    doc = pymupdf.open(cesta)
    rozmery: list[list[float]] = []
    pisma: dict[str, bool] = {}
    strany = []
    for i, stranka in enumerate(doc, start=1):
        rotace = _narovnej(stranka)
        rozmer = [_r(stranka.rect.width), _r(stranka.rect.height)]
        if rozmer not in rozmery:
            rozmery.append(rozmer)
        for f in stranka.get_fonts():
            nazev = _nazev_pisma(f[3])
            pisma[nazev] = pisma.get(nazev, False) or f[1] not in ("", "n/a")
        radky = _radky_textu(stranka)
        zahlavi, cislo, prvni, prvni_top = _zahlavi_cislo_prvni(radky)
        kresby = stranka.get_drawings()
        car = sum(1 for d in kresby for it in d["items"] if it[0] in ("l", "re"))
        obrazku = len(stranka.get_images(full=True))
        cely_text = " ".join(stranka.get_text("text").split())
        pasy = pasy_inkoustu(stranka)
        strany.append({"strana": i, "rotace": rotace, "zahlavi": zahlavi, "cislo_stranky": cislo,
                       "prvni_radek": prvni, "prvni_radek_top": prvni_top,
                       "prvni_pas": pasy[0] if pasy else None,
                       "posledni_pas": pasy[-1] if pasy else None,
                       "slov": len(cely_text.split()), "znaku": len(cely_text),
                       "mimo_okraje": len(_mimo_okraje(radky)),
                       "otazniky": "??" in cely_text,
                       "prazdna": not cely_text and not obrazku and not kresby,
                       "obrazku": obrazku, "car": car})
    return {
        "pdf": cesta,
        "stran": doc.page_count,
        "rozmery": rozmery,
        "pisma": [{"nazev": n, "vlozene": v} for n, v in sorted(pisma.items())],
        "zalozky": [{"uroven": u, "nazev": n, "strana": s} for u, n, s in doc.get_toc()],
        "strany": strany,
    }


def strany(cesta: str, cisla: list[int]) -> dict:
    doc = pymupdf.open(cesta)
    vysledek = []
    for c in cisla:
        stranka = doc[c - 1]
        rotace = _narovnej(stranka)
        trace = stranka.get_texttrace()
        radky = _radky_textu(stranka)
        obrazky = []
        for img in stranka.get_images(full=True):
            for rect in stranka.get_image_rects(img[0]):
                obrazky.append({"bbox": [_r(v) for v in rect], "sirka_px": img[2], "vyska_px": img[3]})
        cary = [{"bbox": [_r(v) for v in d["rect"]]} for d in stranka.get_drawings()]
        mimo = _mimo_okraje(radky)
        vysledek.append({
            "strana": c,
            "rotace": rotace,
            "sirka": _r(stranka.rect.width),
            "vyska": _r(stranka.rect.height),
            "radky": [{"text": r["text"], "bbox": [_r(v) for v in r["bbox"]],
                       "useky": [_usek(s, trace) for s in r["spans"] if s["text"].strip()]}
                      for r in radky],
            "pasy": pasy_inkoustu(stranka),
            "obrazky": obrazky,
            "cary": cary,
            "mimo_okraje": mimo,
        })
    return {"strany": vysledek}


def text(cesta: str, cisla: list[int]) -> dict:
    doc = pymupdf.open(cesta)
    return {"strany": [{"strana": c, "text": doc[c - 1].get_text("text")} for c in cisla]}


def main(argv: list[str]) -> int:
    for proud in (sys.stdout, sys.stderr):  # Windows: výstup do roury jinak v kódové stránce
        if hasattr(proud, "reconfigure"):
            proud.reconfigure(encoding="utf-8")
    if pymupdf is None:
        print("Chybí knihovna PyMuPDF. Nainstaluj ji: pip install pymupdf", file=sys.stderr)
        return 2
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("pdf")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--souhrn", action="store_true")
    g.add_argument("--strany", metavar="ROZSAH")
    g.add_argument("--text", metavar="ROZSAH")
    a = p.parse_args(argv)
    try:
        doc = pymupdf.open(a.pdf)
    except Exception as e:  # chybějící nebo poškozený soubor
        print(f"PDF nelze otevřít: {a.pdf} ({e})", file=sys.stderr)
        return 1
    if doc.needs_pass:
        print(f"PDF nelze otevřít: {a.pdf} je chráněné heslem", file=sys.stderr)
        return 1
    if a.souhrn:
        data = souhrn(a.pdf)
    else:
        pocet = doc.page_count
        try:
            cisla = rozsah(a.strany or a.text, pocet)
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1
        data = strany(a.pdf, cisla) if a.strany else text(a.pdf, cisla)
    json.dump(data, sys.stdout, ensure_ascii=False, separators=(",", ":"))
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
