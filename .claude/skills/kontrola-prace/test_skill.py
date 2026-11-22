"""Testy návodů skillu — SKILL.md, mereni.md a definice subagenta kontrola-casti."""
import re
from pathlib import Path

TU = Path(__file__).resolve().parent
KOREN = TU.parents[2]
PRAVIDLA = KOREN / "docs" / "pravidla"
SKILL = TU / "SKILL.md"
MERENI = TU / "mereni.md"
AGENT = KOREN / ".claude" / "agents" / "kontrola-casti.md"

CESTA = re.compile(r"`((?:stranky|prvky)/[a-z0-9-]+\.md|dokument\.md|latex-chyby\.md)`")


def frontmatter(cesta):
    text = cesta.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, f"{cesta.name}: chybí frontmatter"
    return dict(re.findall(r"^(\w+): (.*)$", m.group(1), re.M))


def test_agent_jen_cte():
    fm = frontmatter(AGENT)
    assert fm["name"] == "kontrola-casti"
    assert fm["description"]
    nastroje = {n.strip() for n in fm["tools"].split(",")}
    assert nastroje <= {"Read", "Grep", "Glob", "Bash"}, nastroje
    assert "Bash" in nastroje and "Read" in nastroje


def test_cesty_pravidel_existuji():
    for soubor in (SKILL, AGENT, MERENI):
        for cesta in CESTA.findall(soubor.read_text(encoding="utf-8")):
            assert (PRAVIDLA / cesta).is_file(), f"{soubor.name}: {cesta} neexistuje"


def test_kazdy_soubor_pravidel_ma_skupinu():
    uvedene = set(CESTA.findall(SKILL.read_text(encoding="utf-8")))
    for cesta in sorted(PRAVIDLA.glob("*/*.md")):
        rel = cesta.relative_to(PRAVIDLA).as_posix()
        assert rel in uvedene, f"{rel} není v žádné skupině SKILL.md"


def test_skill_vola_agenta_a_mereni():
    text = SKILL.read_text(encoding="utf-8")
    assert "kontrola-casti" in text
    assert "mereni.md" in text
    assert "mereni.md" in AGENT.read_text(encoding="utf-8")
    assert "TeX bodech" in MERENI.read_text(encoding="utf-8")
