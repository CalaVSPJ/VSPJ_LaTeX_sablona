"""Testy kontrolního skriptu popisů pravidel. Spuštění: python3 -m pytest -q docs/pravidla"""
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from kontrola import (  # noqa: E402
    KAPITOLY_PRIRUCKY,
    KRITERIA_POSUDKU,
    MATERIALY_SEMINARE,
    PREFIXY,
    STYLY_SABLONY,
    nacti_pravidla,
    zkontroluj,
)

PRAVIDLO = """### OBR-F01 Titulek pod obrázkem
- Pravidlo: Titulek je pod obrázkem, Calibri 10 pt, tučně, na střed.
- Zdroj: šablona styl Titulek; příručka 6.2
- Varianty: —
- Ověření: PDF — řádek pod obrázkem, výška písma ≈ 10 pt
- Štítky: titulek, písmo, měření
"""


def obrazek(formalni=PRAVIDLO, obsahova=""):
    return f"# Obrázek\n\nPopis.\n\n## Rozpoznání\n\nŘádek „Obr. N:“ pod obrázkem.\n\n## Formální\n\n{formalni}\n## Obsahová\n\n{obsahova}"


def soubor(koren: Path, cesta: str, text: str) -> Path:
    p = koren / cesta
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def chyby(koren, uplne=False):
    return "\n".join(zkontroluj(koren, uplne=uplne))


def test_platny_soubor(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek())
    assert zkontroluj(tmp_path) == []
    pravidla = nacti_pravidla(tmp_path)
    assert [p.id for p in pravidla] == ["OBR-F01"]
    assert pravidla[0].kategorie == "formalni"
    assert pravidla[0].pole["Zdroj"] == "šablona styl Titulek; příručka 6.2"


def test_spatny_prefix(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("OBR-F01", "TAB-F01")))
    assert "prefix" in chyby(tmp_path)


def test_duplicitni_id(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO + "\n" + PRAVIDLO))
    assert "duplicitní" in chyby(tmp_path)


def test_duplicitni_id_mezi_soubory(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek())
    soubor(tmp_path, "prvky/tabulka.md", obrazek(PRAVIDLO).replace("# Obrázek", "# Tabulka"))
    # OBR-F01 v tabulka.md je zároveň špatný prefix i duplicita
    assert "duplicitní" in chyby(tmp_path)


def test_obsahove_id_pod_formalni(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("OBR-F01", "OBR-O01")))
    assert "formální" in chyby(tmp_path)


def test_formalni_id_pod_obsahovou(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO, PRAVIDLO.replace("OBR-F01", "OBR-F05")))
    assert "obsahová" in chyby(tmp_path)


def test_obsahove_pravidlo_ok(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO, PRAVIDLO.replace("OBR-F01", "OBR-O01")))
    assert zkontroluj(tmp_path) == []
    assert nacti_pravidla(tmp_path)[1].kategorie == "obsahova"


def test_chybi_pole(tmp_path):
    bez = "\n".join(r for r in PRAVIDLO.splitlines() if not r.startswith("- Ověření")) + "\n"
    soubor(tmp_path, "prvky/obrazek.md", obrazek(bez))
    assert "Ověření" in chyby(tmp_path)


def test_spatne_poradi_poli(tmp_path):
    r = PRAVIDLO.splitlines()
    prehozene = "\n".join([r[0], r[2], r[1], r[3], r[4]]) + "\n"
    soubor(tmp_path, "prvky/obrazek.md", obrazek(prehozene))
    assert "pořadí" in chyby(tmp_path)


def test_neznamo_pole(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO + "- Barva: modrá\n"))
    assert "neznámé pole" in chyby(tmp_path)


def test_poznamka_volitelna(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO + "- Poznámka: Proč.\n"))
    assert zkontroluj(tmp_path) == []


def test_neplatny_zdroj(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("šablona styl Titulek", "internet")))
    assert "zdroj" in chyby(tmp_path)


def test_zdroj_s_poznamkou_v_zavorce(tmp_path):
    t = PRAVIDLO.replace("příručka 6.2", "příručka 3, 6.2 (Tab. 1); Word PDF s. 13 (změřeno); viz DOK-F01")
    soubor(tmp_path, "prvky/obrazek.md", obrazek(t))
    assert zkontroluj(tmp_path) == []


def test_neplatna_kapitola(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("příručka 6.2", "příručka 14")))
    assert "kapitola" in chyby(tmp_path)


def test_strana_mimo_rozsah(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("příručka 6.2", "Word PDF s. 18")))
    assert "strana" in chyby(tmp_path)


VARIANTY_OK = """- Varianty:
  - a) na střed — příručka 3 (Tab. 1)
  - b) vlevo — šablona styl Nadpis 1; Word PDF s. 11
"""


def test_varianty_ok(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("- Varianty: —\n", VARIANTY_OK)))
    assert zkontroluj(tmp_path) == []


def test_varianty_jedna_polozka(tmp_path):
    jedna = "- Varianty:\n  - a) na střed — příručka 3\n"
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("- Varianty: —\n", jedna)))
    assert "aspoň dvě" in chyby(tmp_path)


def test_varianta_bez_zdroje(tmp_path):
    t = VARIANTY_OK.replace(" — příručka 3 (Tab. 1)", "")
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("- Varianty: —\n", t)))
    assert "varianta" in chyby(tmp_path)


def test_neplatne_overeni(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("Ověření: PDF —", "Ověření: oko —")))
    assert "Ověření" in chyby(tmp_path)


def test_overeni_pdf_a_zdroj(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("Ověření: PDF —", "Ověření: PDF + zdroj —")))
    assert zkontroluj(tmp_path) == []


def test_vzorovy_text(tmp_path):
    t = PRAVIDLO.replace("Titulek je pod obrázkem", "Autor Jan Nový")
    soubor(tmp_path, "prvky/obrazek.md", obrazek(t))
    assert "vzorový text" in chyby(tmp_path)


def test_chybi_sekce_obsahova(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek().split("## Obsahová")[0])
    assert "Obsahová" in chyby(tmp_path)


def test_neznamy_soubor(tmp_path):
    soubor(tmp_path, "prvky/obrazky.md", obrazek())
    assert "neznámý soubor" in chyby(tmp_path)


def test_neznamy_odkaz(tmp_path):
    t = PRAVIDLO.replace("příručka 6.2", "příručka 6.2; viz DOK-F07")
    soubor(tmp_path, "prvky/obrazek.md", obrazek(t))
    assert "DOK-F07" not in chyby(tmp_path)  # bez --uplne se odkazy neověřují
    assert "DOK-F07" in chyby(tmp_path, uplne=True)


def uplna_sada(koren: Path):
    """Všechny soubory typů s jedním pravidlem, README s rozporem a úplné pokrytí."""
    for cesta, prefix in PREFIXY.items():
        soubor(koren, cesta, obrazek(PRAVIDLO.replace("OBR-F01", f"{prefix}-F01")))
    soubor(koren, "README.md", "# Pravidla\n\n## Rozpory\n\n| Téma | Příručka | Šablona DOCX / Word PDF | Pravidla |\n|---|---|---|---|\n| Zarovnání | na střed | vlevo | NA1-F01 |\n\n## Další\n")
    radky = [f"| příručka {k} | DOK-F01 |" for k in KAPITOLY_PRIRUCKY]
    radky += [f"| šablona styl {s} | DOK-F01 |" for s in STYLY_SABLONY]
    radky += [f"| šablona oddíl {n} | vynecháno: důvod |" for n in range(1, 8)]
    radky += [f"| posudek {k} | DOK-F01 |" for k in KRITERIA_POSUDKU]
    radky += [f"| materiál {m} | vynecháno: důvod |" for m in MATERIALY_SEMINARE]
    soubor(koren, "pokryti.md", "# Pokrytí\n\n| Zdroj | Pravidla |\n|---|---|\n" + "\n".join(radky) + "\n")


def test_uplna_sada_ok(tmp_path):
    uplna_sada(tmp_path)
    p = tmp_path / "prvky/nadpis-1.md"
    p.write_text(p.read_text().replace("- Varianty: —\n", VARIANTY_OK))
    assert zkontroluj(tmp_path, uplne=True) == []


def test_rozpor_bez_variant(tmp_path):
    uplna_sada(tmp_path)  # NA1-F01 má Varianty: —
    assert "NA1-F01" in chyby(tmp_path, uplne=True)


def test_pokryti_chybi_kapitola(tmp_path):
    uplna_sada(tmp_path)
    p = tmp_path / "pokryti.md"
    p.write_text(p.read_text().replace("| příručka 6.2 | DOK-F01 |\n", ""))
    assert "příručka 6.2" in chyby(tmp_path, uplne=True)


def test_pokryti_neplatne_id(tmp_path):
    uplna_sada(tmp_path)
    p = tmp_path / "pokryti.md"
    p.write_text(p.read_text().replace("| příručka 6.2 | DOK-F01 |", "| příručka 6.2 | OBR-F09 |"))
    assert "OBR-F09" in chyby(tmp_path, uplne=True)


def test_chybi_soubor_typu(tmp_path):
    uplna_sada(tmp_path)
    (tmp_path / "prvky/tabulka.md").unlink()
    assert "prvky/tabulka.md" in chyby(tmp_path, uplne=True)


def test_cli(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek())
    skript = Path(__file__).parent / "kontrola.py"
    r = subprocess.run([sys.executable, str(skript), str(tmp_path)], capture_output=True, text=True)
    assert r.returncode == 0
    assert r.stdout.strip() == "OK: 1 pravidel v 1 souborech"
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("OBR-F01", "TAB-F01")))
    r = subprocess.run([sys.executable, str(skript), str(tmp_path)], capture_output=True, text=True)
    assert r.returncode == 1
    assert "obrazek.md:" in r.stdout


def test_ignoruje_skryte_adresare(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek())
    soubor(tmp_path, ".pytest_cache/README.md", "# cache\n")
    assert zkontroluj(tmp_path) == []


def test_zdroj_rozhodnuti_repa(tmp_path):
    t = PRAVIDLO.replace("- Varianty: —\n", "- Varianty:\n  - a) Calibri — šablona styl Normální\n  - b) Carlito — rozhodnutí repa (README)\n")
    soubor(tmp_path, "prvky/obrazek.md", obrazek(t))
    assert zkontroluj(tmp_path) == []


def test_pokryti_vice_tabulek(tmp_path):
    uplna_sada(tmp_path)
    p = tmp_path / "prvky/nadpis-1.md"
    p.write_text(p.read_text().replace("- Varianty: —\n", VARIANTY_OK))
    p = tmp_path / "pokryti.md"
    p.write_text(p.read_text() + "\n## Pokyny\n\n| Zdroj | Pravidla |\n|---|---|\n| šablona pokyn: něco | DOK-F01 |\n")
    assert zkontroluj(tmp_path, uplne=True) == []


def test_stare_id_bez_pismene(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("OBR-F01", "OBR-01")))
    assert "PREFIX-F01" in chyby(tmp_path)


def test_chybi_stitky(tmp_path):
    bez = "\n".join(r for r in PRAVIDLO.splitlines() if not r.startswith("- Štítky")) + "\n"
    soubor(tmp_path, "prvky/obrazek.md", obrazek(bez))
    assert "Štítky" in chyby(tmp_path)


def test_neznamy_stitek(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("titulek, písmo, měření", "titulek, krása, měření")))
    assert "krása" in chyby(tmp_path)


def test_stitky_bez_zpusobu_overeni(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("titulek, písmo, měření", "titulek, písmo")))
    assert "měření / text / posouzení" in chyby(tmp_path)


def test_chybi_rozpoznani(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek().replace("## Rozpoznání\n\nŘádek „Obr. N:“ pod obrázkem.\n\n", ""))
    assert "Rozpoznání" in chyby(tmp_path)


def test_dokument_bez_rozpoznani(tmp_path):
    text = obrazek(PRAVIDLO.replace("OBR-F01", "DOK-F01")).replace("## Rozpoznání\n\nŘádek „Obr. N:“ pod obrázkem.\n\n", "")
    soubor(tmp_path, "dokument.md", text)
    assert zkontroluj(tmp_path) == []


def test_latex_chyby_soubor(tmp_path):
    text = obrazek(PRAVIDLO.replace("OBR-F01", "LTX-F01")).replace("## Rozpoznání\n\nŘádek „Obr. N:“ pod obrázkem.\n\n", "")
    soubor(tmp_path, "latex-chyby.md", text)
    assert zkontroluj(tmp_path) == []


def _se_zdrojem(tmp_path, zdroj):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("šablona styl Titulek; příručka 6.2", zdroj)))
    return chyby(tmp_path)


def test_zdroj_smernice(tmp_path):
    assert _se_zdrojem(tmp_path, "směrnice SP 2/2020 (čl. 5)") == ""


def test_zdroj_seminar(tmp_path):
    assert _se_zdrojem(tmp_path, "seminář Úvod; seminář Typy BP") == ""


def test_zdroj_seminar_nezname_tema(tmp_path):
    assert "téma" in _se_zdrojem(tmp_path, "seminář Vaření")


def test_zdroj_apa(tmp_path):
    assert _se_zdrojem(tmp_path, "APA manuál") == ""


def test_stitek_styl(tmp_path):
    soubor(tmp_path, "prvky/obrazek.md", obrazek(PRAVIDLO.replace("titulek, písmo, měření", "styl, posouzení")))
    assert zkontroluj(tmp_path) == []


def test_pokryti_chybi_kriterium(tmp_path):
    uplna_sada(tmp_path)
    p = tmp_path / "pokryti.md"
    p.write_text(p.read_text().replace("| posudek Význam pro praxi | DOK-F01 |\n", ""))
    assert "Význam pro praxi" in chyby(tmp_path, uplne=True)


def test_pokryti_chybi_material(tmp_path):
    uplna_sada(tmp_path)
    p = tmp_path / "pokryti.md"
    p.write_text(p.read_text().replace("| materiál desky_bp.pdf | vynecháno: důvod |\n", ""))
    assert "desky_bp.pdf" in chyby(tmp_path, uplne=True)
