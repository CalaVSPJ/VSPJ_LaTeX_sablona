"""Testy vytahni.py na Word PDF šablony (Dokumenty/Sablona.pdf) — známé hodnoty z měření pravidel.

Spuštění: python3 -m pytest -q .claude/skills/kontrola-prace
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

TU = Path(__file__).resolve().parent
sys.path.insert(0, str(TU))
import vytahni  # noqa: E402

KOREN = TU.parents[2]
SABLONA = str(KOREN / "Dokumenty" / "Sablona.pdf")
SKRIPT = str(TU / "vytahni.py")


@pytest.fixture(scope="module")
def souhrn():
    return vytahni.souhrn(SABLONA)


def strana(data, cislo):
    return next(s for s in data["strany"] if s["strana"] == cislo)


def test_rozsah_stran():
    assert vytahni.rozsah("3-5,7", 17) == [3, 4, 5, 7]
    with pytest.raises(ValueError):
        vytahni.rozsah("18", 17)


def test_souhrn_zaklad(souhrn):
    assert souhrn["stran"] == 17
    w, h = souhrn["rozmery"][0]
    assert abs(w - 595.3) < 0.5 and abs(h - 841.9) < 0.5
    nazvy = {p["nazev"].lower().replace(" ", "").replace("-", "") for p in souhrn["pisma"]}
    assert "calibri" in nazvy
    assert "calibrilight" in nazvy


def test_souhrn_zalozky_seznam(souhrn):
    assert isinstance(souhrn["zalozky"], list)


def test_souhrn_zahlavi_a_cislo(souhrn):
    assert "Vysoká škola polytechnická Jihlava" in strana(souhrn, 6)["zahlavi"]
    assert strana(souhrn, 1)["zahlavi"] is None
    assert strana(souhrn, 10)["cislo_stranky"] == "10"
    assert strana(souhrn, 6)["cislo_stranky"] is None


def test_pasy_titulni():
    pasy = vytahni.strany(SABLONA, [1])["strany"][0]["pasy"]
    assert abs(pasy[0]["top"] - 96.5) <= 0.75
    assert any(abs(p["top"] - 360.2) <= 0.75 for p in pasy)


def test_pasy_zahlavi_a_cislo():
    data = vytahni.strany(SABLONA, [6, 10])["strany"]
    zahlavi = data[0]["pasy"][0]
    assert abs(zahlavi["top"] - 38.5) <= 0.75
    assert abs(zahlavi["x0"] - 250) <= 2 and abs(zahlavi["x1"] - 402) <= 2
    cislo = data[1]["pasy"][-1]
    assert abs(cislo["top"] - 796.5) <= 0.75
    assert abs(cislo["x1"] - 523.5) <= 1


def test_useky_nadpis():
    radky = vytahni.strany(SABLONA, [3])["strany"][0]["radky"]
    useky = [u for r in radky for u in r["useky"] if u["text"].strip() == "Abstrakt"]
    assert useky and abs(useky[0]["velikost"] - 18) <= 0.5
    assert useky[0]["vyplnovani"] == "fill+stroke"  # syntetická tučnost Wordu
    telo = [u for r in radky for u in r["useky"] if u["text"].startswith("Vlastní text")]
    assert telo and telo[0]["vyplnovani"] == "fill"
    assert useky[0]["barva"].startswith("#") and len(useky[0]["barva"]) == 7


def test_text():
    assert "Závěr" in vytahni.text(SABLONA, [15])["strany"][0]["text"]


def test_cli_json():
    r = subprocess.run([sys.executable, SKRIPT, SABLONA, "--souhrn"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout)["stran"] == 17


def test_bez_pymupdf(tmp_path):
    systemovy = shutil.which("python3")
    if not systemovy:
        pytest.skip("python3 není v PATH")
    ma = subprocess.run([systemovy, "-I", "-c", "import pymupdf"], capture_output=True)
    if ma.returncode == 0:
        pytest.skip("systémový python3 má pymupdf")
    r = subprocess.run([systemovy, "-I", SKRIPT, SABLONA, "--souhrn"], capture_output=True, text=True)
    assert r.returncode == 2
    assert "pip install pymupdf" in r.stderr


def test_cli_kompaktni():
    r = subprocess.run([sys.executable, SKRIPT, SABLONA, "--strany", "1"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "\n " not in r.stdout  # bez odsazení — šetří kontext
    assert json.loads(r.stdout)["strany"][0]["strana"] == 1


def _pdf(tmp_path, nazev, priprav):
    import pymupdf
    doc = pymupdf.open()
    stranka = doc.new_page(width=595.3, height=841.9)
    priprav(stranka)
    cesta = str(tmp_path / nazev)
    doc.save(cesta)
    return cesta


def test_rozsah_obraceny():
    with pytest.raises(ValueError):
        vytahni.rozsah("5-3", 17)


def test_vyplnovani_soused(tmp_path):
    def priprav(s):
        s.insert_text((100, 100), "Tucny nadpis", fontsize=11, render_mode=2)
        s.insert_text((100, 112.65), "Obycejny radek pod nim", fontsize=11)
    cesta = _pdf(tmp_path, "soused.pdf", priprav)
    useky = [u for r in vytahni.strany(cesta, [1])["strany"][0]["radky"] for u in r["useky"]]
    podle = {u["text"].strip(): u["vyplnovani"] for u in useky}
    assert podle["Tucny nadpis"] == "fill+stroke"
    assert podle["Obycejny radek pod nim"] == "fill"


def test_rotace(tmp_path):
    def priprav(s):
        s.insert_text((100, 80), "Zahlavi", fontsize=11)
        s.insert_text((100, 400), "Text", fontsize=11)
        s.set_rotation(90)
    cesta = _pdf(tmp_path, "rotace.pdf", priprav)
    st = vytahni.strany(cesta, [1])["strany"][0]
    assert st["rotace"] == 90
    assert len(st["pasy"]) >= 2 and st["pasy"][0]["bottom"] < 100
    assert vytahni.souhrn(cesta)["strany"][0]["rotace"] == 90


def test_souhrn_agregaty(souhrn):
    s15 = strana(souhrn, 15)
    assert s15["slov"] > 20 and s15["znaku"] > s15["slov"]
    assert s15["mimo_okraje"] == 0 and s15["otazniky"] is False and s15["prazdna"] is False
    s10 = strana(souhrn, 10)
    assert abs(s10["posledni_pas"]["top"] - 796.5) <= 0.75
    assert abs(strana(souhrn, 6)["prvni_pas"]["top"] - 38.5) <= 0.75


def test_souhrn_prazdna(tmp_path):
    cesta = _pdf(tmp_path, "prazdna.pdf", lambda s: None)
    assert vytahni.souhrn(cesta)["strany"][0]["prazdna"] is True


def test_utf8_vystup_na_windows():
    import os
    env = dict(os.environ, PYTHONIOENCODING="cp1252")
    r = subprocess.run([sys.executable, SKRIPT, SABLONA, "--text", "4"], capture_output=True, text=True, encoding="utf-8", env=env)
    assert r.returncode == 0, r.stderr
    assert "Prohlašuji" in r.stdout


def test_chybejici_soubor():
    r = subprocess.run([sys.executable, SKRIPT, "neexistuje.pdf", "--souhrn"], capture_output=True, text=True)
    assert r.returncode == 1
    assert "nelze otevřít" in r.stderr
