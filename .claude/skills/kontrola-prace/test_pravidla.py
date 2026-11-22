"""Testy pravidla.py — výběr pravidel z docs/pravidla."""
import re
import subprocess
import sys
from pathlib import Path

SKRIPT = str(Path(__file__).resolve().parent / "pravidla.py")


def spust(*argy):
    return subprocess.run([sys.executable, SKRIPT, *argy], capture_output=True, text=True)


def test_id():
    r = spust("--id", "CIT-F01")
    assert r.returncode == 0, r.stderr
    assert "### CIT-F01" in r.stdout and "Varianty" in r.stdout
    assert "### CIT-F02" not in r.stdout


def test_vice_id():
    r = spust("--id", "DOK-F09,UVO-O01")
    assert "### DOK-F09" in r.stdout and "### UVO-O01" in r.stdout


def test_soubor():
    r = spust("--soubor", "stranky/uvod.md")
    assert r.returncode == 0, r.stderr
    assert "UVO-F01" in r.stdout and "## Rozpoznání" in r.stdout


def test_stitek():
    r = spust("--stitek", "měření")
    assert r.returncode == 0, r.stderr
    bloky = [b for b in r.stdout.split("### ")[1:]]
    assert bloky
    for b in bloky:
        stitky = re.search(r"^- Štítky: (.*)$", b, re.M).group(1)
        assert "měření" in [s.strip() for s in stitky.split(",")]


def test_prehled():
    r = spust("--prehled")
    assert r.returncode == 0, r.stderr
    assert "DOK-F01" in r.stdout and "LTX-F01" in r.stdout
    assert len([radek for radek in r.stdout.splitlines() if radek.startswith("| ") and "-" in radek[:12]]) >= 200


def test_nezname_id():
    r = spust("--id", "XYZ-F99")
    assert r.returncode == 1
    assert "XYZ-F99" in r.stderr


def test_holy_nazev_souboru():
    r = spust("--soubor", "zadani.md")
    assert r.returncode == 0, r.stderr
    assert "ZAD-F01" in r.stdout


def test_nezname_stitek():
    r = spust("--stitek", "krása")
    assert r.returncode == 1
    assert "krása" in r.stderr


def test_utf8_vystup_na_windows():
    import os
    env = dict(os.environ, PYTHONIOENCODING="cp1252")
    r = subprocess.run([sys.executable, SKRIPT, "--soubor", "dokument.md"], capture_output=True, text=True, encoding="utf-8", env=env)
    assert r.returncode == 0, r.stderr
    assert "≈" in r.stdout
