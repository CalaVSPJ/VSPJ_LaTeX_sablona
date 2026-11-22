# Kontrolní skill — plán

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Skill `.claude/skills/kontrola-prace/` pro Claude Code, který zkontroluje PDF práce z LaTeX šablony podle `docs/pravidla/` a zapíše hlášení do `output/`.

**Architecture:** `vytahni.py` (PyMuPDF) vytáhne z PDF fakta jako JSON; `pravidla.py` vybírá pravidla přes `docs/pravidla/kontrola.py`; `SKILL.md` vede Clauda: najít PDF → souhrn → typy stránek → varianty → kontrola po částech → hlášení.

**Tech Stack:** Python 3, PyMuPDF (`pymupdf`), pytest, Markdown.

**Spec:** `docs/superpowers/specs/2026-11-22-kontrolni-skill-design.md`

## Global Constraints

- Jediná závislost mimo standardní knihovnu: `pymupdf`. Testy: pytest.
- Jednotky pt, počátek levý horní roh, strany fyzicky od 1.
- Pásy inkoustu: 288 dpi, odstíny šedi, práh 200, mezera 3 px (shodně s měřením pravidel).
- Okraje šablony: text 99,25–523,9 pt vodorovně, 70,9–771,0 pt svisle.
- Skill nic v práci nemění, nesestavuje PDF ani neinstaluje balíčky bez souhlasu; hlášení jen do `output/kontrola_<RRRR-MM-DD_HHMM>.md`.
- Závažnost: chyba / upozornění (seminář, doporučení, posouzení) / poznámka (varianty, nepopsané prvky, rozsah).
- Čeština v SKILL.md, README a výstupech; kód a klíče JSON česky bez diakritiky.
- Vývojové prostředí: venv v pracovní složce (`$S/venv`) s `pymupdf` a `pytest`; do repa se nepřidává.

## Review Focus

1. **LaTeX nadpisy s dopočtenou tučností (FakeBold)** — písmo není „Bold“, takže `tucne` vyjde false; skill nesmí hlásit „nadpis není tučně“. Úkol 1 přidá `vyplnovani` (způsob vykreslení) z `get_texttrace` a úkol 4 ověří na LaTeX PDF; SKILL.md to zmíní.
2. **Velké PDF** — souhrn musí zůstat malý; `--strany` přijímá „3-5,7“; test `test_rozsah_stran`.
3. **PDF bez záložek nebo bez poděkování** — souhrn nesmí spadnout, `zalozky` je seznam (i prázdný); test `test_souhrn_zalozky_seznam`.
4. **Chybějící pymupdf** — `vytahni.py` skončí kódem 2 a hláškou „pip install pymupdf“; test `test_bez_pymupdf` (spuštění s `PYTHONPATH` na prázdnou složku a `-S`/`-I`).
5. **Tištěné vs fyzické číslo strany** — souhrn uvádí obojí (`strana`, `cislo_stranky`); test na Sablona.pdf s. 10 → `cislo_stranky == "10"`.

---

### Task 1: vytahni.py

**Files:** Create `.claude/skills/kontrola-prace/vytahni.py`, `.claude/skills/kontrola-prace/test_vytahni.py`

**Interfaces — Produces:**
- `rozsah(spec: str, pocet: int) -> list[int]` — „3-5,7“ → [3,4,5,7]; mimo 1..pocet → ValueError.
- `pasy_inkoustu(stranka: "fitz.Page", dpi=288, prah=200, mezera=3) -> list[dict]` — `{"top","bottom","x0","x1"}` zaokrouhleno na 0,1 pt.
- `souhrn(cesta: str) -> dict` — `{"pdf","stran","rozmery":[[w,h],…] (unikátní),"pisma":[{"nazev","vlozene"}],"zalozky":[{"uroven","nazev","strana"}],"strany":[{"strana","zahlavi","cislo_stranky","prvni_radek","prvni_radek_top","obrazku","car"}]}`; záhlaví = text řádků s bottom < 70,9; číslo stránky = text řádků s top > 771,0; první řádek = první řádek s top ≥ 60 a bottom ≤ 771.
- `strany(cesta: str, cisla: list[int]) -> dict` — `{"strany":[{"strana","sirka","vyska","radky":[{"text","bbox":[x0,top,x1,bottom],"useky":[{"text","pismo","velikost","tucne","kurziva","barva","vyplnovani"}]}],"pasy":[…],"obrazky":[{"bbox","sirka_px","vyska_px"}],"cary":[{"bbox"}],"mimo_okraje":[{"text","bbox"}]}]}`; `tucne` = příznak bold nebo „Bold“ v názvu písma; `vyplnovani` = "fill" | "stroke" | "fill+stroke" (z `get_texttrace`, kvůli FakeBold); `barva` "#rrggbb"; `mimo_okraje` = řádky textu (mimo záhlaví/zápatí) s x0 < 98,25 nebo x1 > 524,9.
- `text(cesta: str, cisla: list[int]) -> dict` — `{"strany":[{"strana","text"}]}`.
- CLI: `vytahni.py PDF (--souhrn | --strany SPEC | --text SPEC)` → JSON na stdout (UTF-8, `ensure_ascii=False`); bez pymupdf exit 2 + hláška s `pip install pymupdf`.

- [ ] **Step 1: venv** `python3 -m venv $S/venv && $S/venv/bin/pip install pymupdf pytest` → import fitz OK.
- [ ] **Step 2: Testy** (fixture `SABLONA = <repo>/Dokumenty/Sablona.pdf`):
  - `test_rozsah_stran`: `rozsah("3-5,7", 17) == [3,4,5,7]`; `rozsah("18", 17)` → ValueError.
  - `test_souhrn_zaklad`: stran 17; rozměry ≈ [595,3, 841,9] (±0,5); názvy písem obsahují „Calibri“ i „Calibri Light“ (normalizace: bez prefixu subsetu `ABCDEF+`, porovnat bez mezer, case-insensitive).
  - `test_souhrn_zalozky_seznam`: `isinstance(s["zalozky"], list)`.
  - `test_souhrn_zahlavi_a_cislo`: s. 6 `zahlavi` obsahuje „Vysoká škola polytechnická Jihlava“; s. 1 `zahlavi is None`; s. 10 `cislo_stranky == "10"`; s. 6 `cislo_stranky is None`.
  - `test_pasy_titulni`: s. 1 první pás top 96,5 ±0,75; pás s top 360,2 ±0,75 existuje.
  - `test_pasy_zahlavi_a_cislo`: s. 6 pás top 38,5 ±0,75, x0 250 ±2, x1 402 ±2; s. 10 pás top 796,5 ±0,75, x1 523,5 ±1.
  - `test_useky_nadpis`: s. 3 úsek s textem „Abstrakt“ má velikost 18 ±0,5.
  - `test_text`: `text(SABLONA,[15])` obsahuje „Závěr“.
  - `test_cli_json`: `subprocess` `--souhrn` → validní JSON, `stran == 17`.
  - `test_bez_pymupdf`: spustit `python3 -I vytahni.py X --souhrn` s interpretem bez pymupdf (systémový `python3`, kde fitz není) → exit 2, stderr obsahuje „pip install pymupdf“. Pokud systémový python fitz má, test přeskočit (`pytest.skip`).
- [ ] **Step 3:** `$S/venv/bin/python -m pytest -q .claude/skills/kontrola-prace` → FAIL (modul chybí).
- [ ] **Step 4:** Implementovat. Pásy: `page.get_pixmap(dpi=288, colorspace=fitz.csGRAY)`, řádek obrazu je „inkoust“, když některý pixel (krok 2 px) < práh; spojit řádky s mezerou ≤ 3 px; x0/x1 z pixelů pásu. Úseky z `page.get_text("dict")`; `vyplnovani` párovat podle bbox z `page.get_texttrace()` (typ 0 = fill, 1 = stroke, jinak fill+stroke; bez shody "fill").
- [ ] **Step 5:** testy PASS. **Step 6: Commit** — `feat(skill): vytahni.py — fakta z PDF`.

### Task 2: pravidla.py

**Files:** Create `.claude/skills/kontrola-prace/pravidla.py`, `.claude/skills/kontrola-prace/test_pravidla.py`

**Interfaces — Consumes:** `docs/pravidla/kontrola.py`: `nacti_pravidla(koren) -> list[Pravidlo]` (`id`, `nazev`, `kategorie`, `pole`, `soubor`, `radek`, `varianty`).
**Produces:** CLI `pravidla.py (--prehled | --soubor CESTA | --id ID[,ID…] | --stitek STITEK)`; `--soubor` vypíše soubor tak, jak je (Markdown); `--id`/`--stitek` vypíšou Markdown bloky pravidel (nadpis + pole + varianty) v pořadí souborů; `--prehled` tabulka `ID | název | soubor | štítky jak`.

- [ ] **Step 1: Testy:** `test_id` (`--id CIT-F01` → obsahuje „### CIT-F01“ a „Varianty“, neobsahuje „### CIT-F02“); `test_soubor` (`--soubor stranky/uvod.md` obsahuje „UVO-F01“ a „## Rozpoznání“); `test_stitek` (`--stitek měření` — každý blok má ve Štítcích „měření“); `test_prehled` (obsahuje „DOK-F01“ a „LTX-F01“, řádků ≥ 200); `test_nezname_id` (exit 1, stderr obsahuje ID).
- [ ] **Step 2:** FAIL. **Step 3:** Implementovat (import `kontrola` z `<repo>/docs/pravidla` přes `sys.path`; kořen repa = 3 úrovně nad souborem). **Step 4:** PASS. **Step 5: Commit** — `feat(skill): pravidla.py — výběr pravidel`.

### Task 3: SKILL.md, README.md, odkazy

**Files:** Create `.claude/skills/kontrola-prace/SKILL.md`, `.claude/skills/kontrola-prace/README.md`; Modify `README.md` (struktura repa + krátká sekce „Kontrola práce“), `docs/README.md` (odkaz na skill).

- [ ] **Step 1: SKILL.md** — frontmatter `name: kontrola-prace`, `description:` (česky; spouštěcí slova: zkontroluj práci, kontrola práce, zkontroluj úvod/citace/formát…). Tělo ≤ ~150 řádků: zásady (jen upozorňuje, nic nemění, stupeň 2 MP 8/2026; neodhadovat čísla, odkazovat ID), krok 1–8 ze specifikace s přesnými příkazy (`python3 .claude/skills/kontrola-prace/vytahni.py …`, `pravidla.py …`), mapování typ stránky → soubor pravidel, pravidla závažnosti, šablona hlášení ze specifikace, poznámka k FakeBold (u LaTeX nadpisů rozhoduje `vyplnovani` / pás inkoustu, ne název písma), záložní režim bez pymupdf, režimy (celá / část / jen F / jen O).
- [ ] **Step 2: README.md** (krátké): Jak funguje / Jak ho přidat (fork, Claude Code v kořeni, `pip install pymupdf`, případně venv) / Jak ho použít (sestavit PDF, příkazy, kde je hlášení, osobní a důvěrné údaje). Odkaz na `docs/pravidla/README.md` a na MP 8/2026.
- [ ] **Step 3:** Kořenové README a `docs/README.md` — odkazy.
- [ ] **Step 4: Ověření** `$S/venv/bin/python -m pytest -q .claude/skills/kontrola-prace docs/pravidla` → PASS; `python3 docs/pravidla/kontrola.py --uplne` → OK.
- [ ] **Step 5: Commit** — `feat(skill): SKILL.md a README`.

### Task 4: Ověření na skutečném PDF

**Files:** Modify podle nálezů `SKILL.md` / `vytahni.py` (+ test, pokud jde o kód).

- [ ] **Step 1:** `vytahni.py Verze/prace_22-11-2026_1327.pdf --souhrn` → JSON; zkontrolovat záložky (hyperref), záhlaví, čísla stran.
- [ ] **Step 2:** `--strany 11` na tomtéž PDF: nadpis kapitoly — hodnota `tucne` a `vyplnovani`; zapsat do ledgeru, zda FakeBold jde rozpoznat. Pokud ne, upravit SKILL.md (tučnost nadpisů v LaTeX PDF neposuzovat podle názvu písma).
- [ ] **Step 3:** Projít postup SKILL.md ručně (jako skill) na tomto PDF pro titulní stranu a stranu 6–11 a vytvořit `output/kontrola_….md`; očekávaný nález DOK-F08 (záhlaví na středu místo tabulátoru 226,8 pt → ≈ 14 pt rozdíl).
- [ ] **Step 4:** Úpravy SKILL.md podle zkušenosti (nejasné kroky, chybějící příkaz). Testy PASS.
- [ ] **Step 5: Commit** — `fix(skill): úpravy po ověření na PDF šablony`.
