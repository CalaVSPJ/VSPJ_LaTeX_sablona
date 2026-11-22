#!/usr/bin/env python3
"""Kontrola formátu popisů pravidel v docs/pravidla/.

Použití:
    python3 docs/pravidla/kontrola.py            # formát existujících souborů
    python3 docs/pravidla/kontrola.py --uplne    # navíc úplnost, odkazy, rozpory, pokrytí

Kontroluje jen formu popisů (ID, pole, odkazy na zdroje), ne správnost pravidel.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

PREFIXY: dict[str, str] = {
    "dokument.md": "DOK",
    "stranky/titulni-strana.md": "TIT",
    "stranky/zadani.md": "ZAD",
    "stranky/abstrakt.md": "ABS",
    "stranky/prohlaseni.md": "PRO",
    "stranky/podekovani.md": "POD",
    "stranky/obsah.md": "OBS",
    "stranky/seznam-obrazku.md": "SOB",
    "stranky/seznam-tabulek.md": "STA",
    "stranky/seznam-zkratek.md": "SZK",
    "stranky/uvod.md": "UVO",
    "stranky/kapitola.md": "KAP",
    "stranky/zaver.md": "ZAV",
    "stranky/seznam-literatury.md": "LIT",
    "stranky/prilohy.md": "PRI",
    "prvky/nadpis-1.md": "NA1",
    "prvky/nadpis-2.md": "NA2",
    "prvky/nadpis-3.md": "NA3",
    "prvky/obrazek.md": "OBR",
    "prvky/tabulka.md": "TAB",
    "prvky/rovnice.md": "ROV",
    "prvky/vycet-seznam.md": "VYC",
    "prvky/odkaz-v-textu.md": "CIT",
    "prvky/poznamka-pod-carou.md": "PPC",
    "prvky/polozka-literatury.md": "BIB",
    "latex-chyby.md": "LTX",
}

# Soubory bez oddílu „## Rozpoznání“ (nepopisují jednu stránku ani prvek)
BEZ_ROZPOZNANI = {"dokument.md", "latex-chyby.md"}

# Štítky — čeho se pravidlo týká a jak se ověřuje (popis v README)
STITKY_CO: list[str] = [
    "písmo", "barva", "zarovnání", "řádkování", "mezery", "odsazení", "poloha",
    "stránkování", "číslování-stránek", "záhlaví", "číslování", "nadpis", "titulek",
    "zdroj", "obrázek", "tabulka", "rovnice", "výčet", "poznámka", "interpunkce",
    "uvozovky", "pomlčky", "pevné-mezery", "dělení-slov", "čísla-a-jednotky",
    "zkratky", "citace", "literatura", "struktura", "jednotnost", "obsah-textu", "styl", "latex",
]
STITKY_JAK: list[str] = ["měření", "text", "posouzení", "zdrojový-soubor"]

# Kapitoly příručky „Jak psát práce na VŠPJ“ (2021)
KAPITOLY_PRIRUCKY: list[str] = [
    "1", "1.1", "1.2", "1.3", "2", "3",
    "4", "4.1", "4.2", "4.3", "4.4", "4.5",
    "5", "5.1", "5.2", "5.3",
    "6", "6.1", "6.2", "6.3",
    "7", "7.1", "7.2", "7.3",
    "8", "9", "10", "11", "11.1", "11.2", "12", "13",
]

STYLY_SABLONY: list[str] = [
    "Normální", "Nadpis 1", "Nadpis 2", "Nadpis 3", "Název", "Titulek", "Zdroj",
    "Tabulka", "Seznam literatury", "Obsah 1", "Obsah 2", "Text poznámky pod čarou",
]

ODDILY_SABLONY = range(1, 8)

# Témata materiálů Semináře k bakalářské práci (KTS) — zdroj „seminář <téma>“
SEMINAR_TEMATA: list[str] = [
    "Úvod", "Závěr", "Abstrakt", "Typy BP", "Rešerše", "Citace", "Typografie", "Chyby", "Vyhledávání",
]

# Kritéria posudku vedoucího a oponenta (Směrnice SP 2/2020, příloha 1 a 2)
KRITERIA_POSUDKU: list[str] = [
    "Splnění stanovených cílů závěrečné práce",
    "Význam pro praxi",
    "Aktuálnost zvoleného tématu",
    "Použité metody zpracování",
    "Metody hodnocení výsledků",
    "Struktura práce",
    "Práce s odbornou literaturou a citace",
    "Stylistická kvalita závěrečné práce a formální úroveň textu",
    "Aktivita a práce studenta při vypracování závěrečné práce",
]

# Soubory materiálů semináře SBP (mimo šablonu a příručku, které jsou zdrojem zvlášť)
MATERIALY_SEMINARE: list[str] = [
    "Citační manuál APA.pdf", "Matematicka_sazba_c3.pdf", "SBP_CVIČ2.pptx", "Směrnice BP 2020.pdf",
    "abstrakt.doc", "chyby_v__pracich.ppt", "citace 2.pptx", "citace.ppt", "co_ma_byt_v_zaveru.doc",
    "desky_bp.pdf", "harmonogram_ZP_leden_27.docx", "harvard odkazy.pdf", "prohlaseni.doc",
    "psaní závěru.pptx", "rešerše.docx", "sbp7_abstrakt.pptx", "sbp_cvič1.ppt", "sbp_rešerše.pptx",
    "tipy_na_vyhledávání.pdf", "typografie.pdf", "typografie_prezentace.pptx", "uvod.doc",
]
STRAN_WORD_PDF = 17
POVINNA_POLE = ["Pravidlo", "Zdroj", "Varianty", "Ověření", "Štítky"]
VOLITELNA_POLE = ["Poznámka"]
VZOROVY_TEXT = ["Jan Nový", "Starý", "Vlastní text"]
NESOUBORY = {"README.md", "pokryti.md"}

RE_PRAVIDLO = re.compile(r"^### ([A-Z0-9]{3})-([FO])(\d{2}) (\S.*)$")
RE_POLE = re.compile(r"^- ([^:]+):(.*)$")
RE_VARIANTA = re.compile(r"^  - [a-z]\) (.+)$")
RE_ID = re.compile(r"\b[A-Z][A-Z0-9]{2}-[FO]\d{2}\b")
RE_OVERENI = re.compile(r"^(PDF \+ zdroj|PDF|zdroj) — \S")
RE_WORD_PDF = re.compile(r"^Word PDF s\. (\d+)(?:[–-](\d+))?$")


@dataclass
class Pravidlo:
    id: str
    nazev: str
    kategorie: Literal["formalni", "obsahova"]
    pole: dict[str, str]
    soubor: Path
    radek: int
    poradi: list[str] = field(default_factory=list)
    varianty: list[tuple[int, str]] = field(default_factory=list)


def _relativni(koren: Path, p: Path) -> str:
    return p.relative_to(koren).as_posix()


def _soubory_typu(koren: Path) -> list[Path]:
    return sorted(
        p for p in koren.rglob("*.md")
        if (p.name not in NESOUBORY or p.parent != koren)
        and not any(c.startswith(".") for c in p.relative_to(koren).parts)
    )


def _rozeber_soubor(koren: Path, p: Path, chyby: list[str]) -> list[Pravidlo]:
    rel = _relativni(koren, p)
    radky = p.read_text(encoding="utf-8").splitlines()
    pravidla: list[Pravidlo] = []
    kategorie: str | None = None
    sekce: list[str] = []
    aktualni: Pravidlo | None = None
    posledni_pole: str | None = None

    neprazdne = [r for r in radky if r.strip()]
    if not neprazdne or not neprazdne[0].startswith("# "):
        chyby.append(f"{rel}:1: soubor musí začínat nadpisem „# Název typu“")

    for i, radek in enumerate(radky, start=1):
        if radek.startswith("## "):
            aktualni = None
            nazev = radek[3:].strip()
            if nazev == "Formální":
                kategorie = "formalni"
            elif nazev == "Obsahová":
                kategorie = "obsahova"
            else:
                kategorie = None
            sekce.append(nazev)
            continue
        if radek.startswith("### "):
            m = RE_PRAVIDLO.match(radek)
            if not m:
                chyby.append(f"{rel}:{i}: nadpis pravidla musí mít tvar „### PREFIX-F01 Název“ (F formální, O obsahová)")
                aktualni = None
                continue
            if kategorie is None:
                chyby.append(f"{rel}:{i}: pravidlo mimo sekci ## Formální / ## Obsahová")
                aktualni = None
                continue
            aktualni = Pravidlo(
                id=f"{m.group(1)}-{m.group(2)}{m.group(3)}", nazev=m.group(4),
                kategorie=kategorie, pole={}, soubor=p, radek=i,
            )
            pravidla.append(aktualni)
            posledni_pole = None
            continue
        if aktualni is None or not radek.strip():
            continue
        m = RE_POLE.match(radek)
        if m:
            posledni_pole = m.group(1).strip()
            aktualni.pole[posledni_pole] = m.group(2).strip()
            aktualni.poradi.append(posledni_pole)
            continue
        mv = RE_VARIANTA.match(radek)
        if mv and posledni_pole == "Varianty":
            aktualni.varianty.append((i, mv.group(1)))
            continue
        if posledni_pole:  # pokračování víceřádkového pole
            aktualni.pole[posledni_pole] += " " + radek.strip()

    for nazev in ("Formální", "Obsahová"):
        if nazev not in sekce:
            chyby.append(f"{rel}:1: chybí sekce „## {nazev}“")
    if "Formální" in sekce and "Obsahová" in sekce and sekce.index("Formální") > sekce.index("Obsahová"):
        chyby.append(f"{rel}:1: sekce ## Formální musí být před ## Obsahová")
    if rel not in BEZ_ROZPOZNANI:
        if "Rozpoznání" not in sekce:
            chyby.append(f"{rel}:1: chybí sekce „## Rozpoznání“ (jak skill stránku / prvek v PDF najde)")
        elif "Formální" in sekce and sekce.index("Rozpoznání") > sekce.index("Formální"):
            chyby.append(f"{rel}:1: sekce ## Rozpoznání musí být před ## Formální")
    return pravidla


def _zkontroluj_zdroj(text: str) -> list[str]:
    """Vrátí seznam problémů v textu zdroje (části oddělené středníkem)."""
    problemy = []
    for cast in (c.strip() for c in text.split(";")):
        jadro = re.sub(r"\s*\([^)]*\)$", "", cast).strip()
        if jadro.startswith("příručka "):
            for kap in (k.strip() for k in jadro[len("příručka "):].split(",")):
                if kap not in KAPITOLY_PRIRUCKY:
                    problemy.append(f"neznámá kapitola příručky „{kap}“")
        elif jadro.startswith("šablona ") and len(jadro) > len("šablona "):
            pass
        elif m := RE_WORD_PDF.match(jadro):
            for s in (m.group(1), m.group(2)):
                if s is not None and not 1 <= int(s) <= STRAN_WORD_PDF:
                    problemy.append(f"strana Word PDF {s} mimo 1–{STRAN_WORD_PDF}")
        elif re.fullmatch(r"viz [A-Z][A-Z0-9]{2}-[FO]\d{2}", jadro):
            pass
        elif jadro in ("rozhodnutí repa", "směrnice SP 2/2020", "APA manuál"):
            pass
        elif jadro.startswith("seminář "):
            if jadro[len("seminář "):] not in SEMINAR_TEMATA:
                problemy.append(f"neznámé téma semináře „{jadro[len('seminář '):]}“ (seznam SEMINAR_TEMATA)")
        else:
            problemy.append(f"neplatný zdroj „{cast}“ (příručka X / šablona … / Word PDF s. N / viz ID / rozhodnutí repa / směrnice SP 2/2020 / seminář <téma> / APA manuál)")
    return problemy


def _zkontroluj_pravidlo(koren: Path, pr: Pravidlo, chyby: list[str]) -> None:
    rel = f"{_relativni(koren, pr.soubor)}:{pr.radek}"
    cislo = int(pr.id[-2:])
    ocekavany = PREFIXY.get(_relativni(koren, pr.soubor))
    if ocekavany and pr.id[:3] != ocekavany:
        chyby.append(f"{rel}: prefix {pr.id[:3]} neodpovídá souboru (čekáno {ocekavany})")
    if pr.kategorie == "formalni" and pr.id[4] != "F":
        chyby.append(f"{rel}: {pr.id} — pod ## Formální patří ID s F (formální)")
    if pr.kategorie == "obsahova" and pr.id[4] != "O":
        chyby.append(f"{rel}: {pr.id} — pod ## Obsahová patří ID s O (obsahová)")
    if cislo < 1:
        chyby.append(f"{rel}: {pr.id} — čísla pravidel začínají 01")

    for nazev in pr.poradi:
        if nazev not in POVINNA_POLE + VOLITELNA_POLE:
            chyby.append(f"{rel}: {pr.id} — neznámé pole „{nazev}“")
    for nazev in POVINNA_POLE:
        if nazev not in pr.pole:
            chyby.append(f"{rel}: {pr.id} — chybí pole „{nazev}“")
    znama = [n for n in pr.poradi if n in POVINNA_POLE + VOLITELNA_POLE]
    if znama != [n for n in POVINNA_POLE + VOLITELNA_POLE if n in znama]:
        chyby.append(f"{rel}: {pr.id} — špatné pořadí polí (Pravidlo, Zdroj, Varianty, Ověření, Štítky, Poznámka)")

    if "Štítky" in pr.pole:
        stitky = [t.strip() for t in pr.pole["Štítky"].split(",") if t.strip()]
        for t in stitky:
            if t not in STITKY_CO + STITKY_JAK:
                chyby.append(f"{rel}: {pr.id} — neznámý štítek „{t}“ (seznam v README)")
        if not any(t in STITKY_JAK for t in stitky):
            chyby.append(f"{rel}: {pr.id} — Štítky musí obsahovat způsob ověření (měření / text / posouzení / zdrojový-soubor)")

    for vzor in VZOROVY_TEXT:
        if vzor in pr.pole.get("Pravidlo", ""):
            chyby.append(f"{rel}: {pr.id} — vzorový text ze šablony „{vzor}“ v pravidle")

    if "Zdroj" in pr.pole:
        if not pr.pole["Zdroj"]:
            chyby.append(f"{rel}: {pr.id} — prázdný zdroj")
        for problem in _zkontroluj_zdroj(pr.pole["Zdroj"]):
            chyby.append(f"{rel}: {pr.id} — {problem}")

    if "Varianty" in pr.pole:
        hodnota = pr.pole["Varianty"]
        if hodnota == "—":
            if pr.varianty:
                chyby.append(f"{rel}: {pr.id} — Varianty: „—“ nesmí mít položky")
        elif hodnota:
            chyby.append(f"{rel}: {pr.id} — Varianty jsou „—“ nebo seznam „  - a) … — zdroj“")
        else:
            if len(pr.varianty) < 2:
                chyby.append(f"{rel}: {pr.id} — Varianty: potřeba aspoň dvě varianty")
            for i, text in pr.varianty:
                if " — " not in text:
                    chyby.append(f"{_relativni(koren, pr.soubor)}:{i}: {pr.id} — varianta bez zdroje („… — zdroj“)")
                    continue
                for problem in _zkontroluj_zdroj(text.rsplit(" — ", 1)[1]):
                    chyby.append(f"{_relativni(koren, pr.soubor)}:{i}: {pr.id} — varianta: {problem}")

    if "Ověření" in pr.pole and not RE_OVERENI.match(pr.pole["Ověření"]):
        chyby.append(f"{rel}: {pr.id} — Ověření musí začínat „PDF — “, „zdroj — “ nebo „PDF + zdroj — “")


def nacti_pravidla(koren: Path) -> list[Pravidlo]:
    koren = Path(koren)
    pravidla: list[Pravidlo] = []
    for p in _soubory_typu(koren):
        pravidla += _rozeber_soubor(koren, p, [])
    return pravidla


def _tabulka(radky: list[str]) -> list[tuple[int, list[str]]]:
    """Řádky Markdown tabulek jako (číslo řádku, buňky), bez záhlaví a oddělovačů.

    Záhlaví = řádek tabulky, za kterým následuje oddělovač |---|; tabulek může být víc.
    """
    tabulkove = []
    for i, r in radky:
        if r.startswith("|"):
            tabulkove.append((i, [b.strip() for b in r.strip().strip("|").split("|")]))
    def oddelovac(bunky):
        return all(re.fullmatch(r":?-+:?", b) for b in bunky)
    vysledek = []
    for k, (i, bunky) in enumerate(tabulkove):
        if oddelovac(bunky):
            continue
        dalsi = tabulkove[k + 1] if k + 1 < len(tabulkove) else None
        if dalsi and dalsi[0] == i + 1 and oddelovac(dalsi[1]):
            continue  # záhlaví
        vysledek.append((i, bunky))
    return vysledek


def _sekce(text: str, nadpis: str) -> list[tuple[int, str]]:
    radky = text.splitlines()
    uvnitr, vysledek = False, []
    for i, r in enumerate(radky, start=1):
        if r.startswith("## "):
            uvnitr = r[3:].strip() == nadpis
            continue
        if uvnitr:
            vysledek.append((i, r))
    return vysledek


def _zkontroluj_uplne(koren: Path, podle_id: dict[str, Pravidlo], chyby: list[str]) -> None:
    for cesta in PREFIXY:
        if not (koren / cesta).exists():
            chyby.append(f"{cesta}:0: chybí soubor typu {cesta}")

    for pr in podle_id.values():
        texty = [pr.pole.get(n, "") for n in POVINNA_POLE + VOLITELNA_POLE] + [t for _, t in pr.varianty]
        for odkaz in sorted({o for t in texty for o in RE_ID.findall(t)}):
            if odkaz not in podle_id:
                chyby.append(f"{_relativni(koren, pr.soubor)}:{pr.radek}: {pr.id} — odkaz na neexistující {odkaz}")

    readme = koren / "README.md"
    if not readme.exists():
        chyby.append("README.md:0: chybí README.md")
    else:
        radky = _tabulka(_sekce(readme.read_text(encoding="utf-8"), "Rozpory"))
        if not radky:
            chyby.append("README.md:0: chybí tabulka v sekci „## Rozpory“")
        for i, bunky in radky:
            ids = RE_ID.findall(bunky[-1])
            if not ids:
                chyby.append(f"README.md:{i}: rozpor „{bunky[0]}“ nemá vyplněná pravidla")
            for x in ids:
                if x not in podle_id:
                    chyby.append(f"README.md:{i}: rozpor odkazuje na neexistující {x}")
                elif podle_id[x].pole.get("Varianty", "—") == "—":
                    chyby.append(f"README.md:{i}: rozpor odkazuje na {x}, které nemá varianty")

    pokryti = koren / "pokryti.md"
    if not pokryti.exists():
        chyby.append("pokryti.md:0: chybí pokryti.md")
        return
    radky = _tabulka(list(enumerate(pokryti.read_text(encoding="utf-8").splitlines(), start=1)))
    zdroje = {}
    for i, bunky in radky:
        zdroje[bunky[0]] = (i, bunky[-1])
    pozadovane = [f"příručka {k}" for k in KAPITOLY_PRIRUCKY]
    pozadovane += [f"šablona styl {s}" for s in STYLY_SABLONY]
    pozadovane += [f"šablona oddíl {n}" for n in ODDILY_SABLONY]
    pozadovane += [f"posudek {k}" for k in KRITERIA_POSUDKU]
    pozadovane += [f"materiál {m}" for m in MATERIALY_SEMINARE]
    for klic in pozadovane:
        if klic not in zdroje:
            chyby.append(f"pokryti.md:0: pokrytí — chybí řádek „{klic}“")
    for klic, (i, hodnota) in zdroje.items():
        if hodnota.startswith("vynecháno:") and hodnota[len("vynecháno:"):].strip():
            continue
        ids = RE_ID.findall(hodnota)
        if not ids:
            chyby.append(f"pokryti.md:{i}: „{klic}“ — uveď ID pravidel nebo „vynecháno: důvod“")
        for x in ids:
            if x not in podle_id:
                chyby.append(f"pokryti.md:{i}: „{klic}“ odkazuje na neexistující {x}")


def zkontroluj(koren: Path, uplne: bool = False) -> list[str]:
    koren = Path(koren)
    chyby: list[str] = []
    podle_id: dict[str, Pravidlo] = {}
    for p in _soubory_typu(koren):
        rel = _relativni(koren, p)
        if rel not in PREFIXY:
            chyby.append(f"{rel}:0: neznámý soubor (není v seznamu typů PREFIXY)")
        for pr in _rozeber_soubor(koren, p, chyby):
            _zkontroluj_pravidlo(koren, pr, chyby)
            if pr.id in podle_id:
                drive = podle_id[pr.id]
                chyby.append(
                    f"{rel}:{pr.radek}: duplicitní ID {pr.id} "
                    f"(už v {_relativni(koren, drive.soubor)}:{drive.radek})"
                )
            else:
                podle_id[pr.id] = pr
    if uplne:
        _zkontroluj_uplne(koren, podle_id, chyby)
    return chyby


def main(argv: list[str]) -> int:
    uplne = "--uplne" in argv
    ostatni = [a for a in argv if a != "--uplne"]
    koren = Path(ostatni[0]) if ostatni else Path(__file__).resolve().parent
    chyby = zkontroluj(koren, uplne=uplne)
    if chyby:
        print("\n".join(chyby))
        return 1
    soubory = [p for p in _soubory_typu(koren)]
    print(f"OK: {len(nacti_pravidla(koren))} pravidel v {len(soubory)} souborech")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
