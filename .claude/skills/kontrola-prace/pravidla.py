#!/usr/bin/env python3
"""Výběr pravidel z docs/pravidla pro kontrolní skill.

Použití:
    python3 pravidla.py --prehled                  # tabulka ID | název | soubor | jak se ověřuje
    python3 pravidla.py --soubor stranky/uvod.md   # celý soubor pravidel
    python3 pravidla.py --id CIT-F01,DOK-F09       # jen vybraná pravidla
    python3 pravidla.py --stitek měření            # pravidla se štítkem
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.dont_write_bytecode = True

KOREN = Path(__file__).resolve().parents[3]
PRAVIDLA = KOREN / "docs" / "pravidla"
sys.path.insert(0, str(PRAVIDLA))
from kontrola import STITKY_CO, STITKY_JAK, nacti_pravidla  # noqa: E402


def _blok(pr) -> str:
    """Markdown blok pravidla tak, jak je v souboru (od nadpisu po další nadpis)."""
    radky = pr.soubor.read_text(encoding="utf-8").splitlines()
    konec = pr.radek
    while konec < len(radky) and not radky[konec].startswith(("### ", "## ")):
        konec += 1
    return "\n".join(radky[pr.radek - 1:konec]).rstrip() + "\n"


def _stitky(pr) -> list[str]:
    return [s.strip() for s in pr.pole.get("Štítky", "").split(",") if s.strip()]


def _najdi_soubor(nazev: str) -> Path | None:
    """Cesta relativně k docs/pravidla, nebo jen název souboru (zadani.md)."""
    cesta = PRAVIDLA / nazev
    if cesta.is_file():
        return cesta
    shody = [p for p in PRAVIDLA.rglob(Path(nazev).name) if not p.name.startswith(".")]
    return shody[0] if len(shody) == 1 else None


def main(argv: list[str]) -> int:
    for proud in (sys.stdout, sys.stderr):  # Windows: výstup do roury jinak v kódové stránce
        if hasattr(proud, "reconfigure"):
            proud.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--prehled", action="store_true")
    g.add_argument("--soubor")
    g.add_argument("--id")
    g.add_argument("--stitek")
    a = p.parse_args(argv)

    if a.soubor:
        cesta = _najdi_soubor(a.soubor)
        if cesta is None:
            print(f"neznámý soubor pravidel: {a.soubor}", file=sys.stderr)
            return 1
        print(cesta.read_text(encoding="utf-8"), end="")
        return 0

    pravidla = nacti_pravidla(PRAVIDLA)
    if a.prehled:
        print("| ID | název | soubor | jak |")
        print("|---|---|---|---|")
        for pr in pravidla:
            jak = ", ".join(s for s in _stitky(pr) if s in STITKY_JAK)
            print(f"| {pr.id} | {pr.nazev} | {pr.soubor.relative_to(PRAVIDLA).as_posix()} | {jak} |")
        return 0
    if a.id:
        hledana = [x.strip() for x in a.id.split(",") if x.strip()]
        podle_id = {pr.id: pr for pr in pravidla}
        chybi = [x for x in hledana if x not in podle_id]
        if chybi:
            print(f"neznámé ID: {', '.join(chybi)}", file=sys.stderr)
            return 1
        vybrana = [podle_id[x] for x in hledana]
    else:
        if a.stitek not in STITKY_CO + STITKY_JAK:
            print(f"neznámý štítek: {a.stitek}", file=sys.stderr)
            return 1
        vybrana = [pr for pr in pravidla if a.stitek in _stitky(pr)]
    print("\n".join(_blok(pr) for pr in vybrana), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
