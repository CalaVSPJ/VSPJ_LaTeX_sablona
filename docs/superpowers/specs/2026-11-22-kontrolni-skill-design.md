# Kontrolní skill závěrečné práce — návrh

Datum: 2026-11-22
Stav: schváleno (2026-11-22)
Navazuje na: `2026-11-22-pravidla-prace-design.md`, `2026-11-22-obsahova-pravidla-design.md`

## Záměr

Student si forkne tento repozitář, v lokální kopii píše bakalářskou nebo
diplomovou práci v LaTeX šabloně, sestaví PDF a v Claude Code spustí skill,
který práci zkontroluje podle pravidel v `docs/pravidla/`. Skill **jen
upozorňuje** — vypíše možné nedostatky ve formě i obsahu s odkazy na ID
pravidel; nic v práci nepřepisuje. Tím odpovídá stupni 2 (Asistence) podle
MP č. 8/2026, který je u závěrečné práce nejvyšší přípustný, pokud vedoucí nestanovil jinak.

## Cíle

- Skill v repu: `.claude/skills/kontrola-prace/` (Claude Code ho najde sám,
  když student otevře Claude Code v kořeni repa).
- Krátké `README.md` u skillu: jak funguje, jak ho přidat (zprovoznit), jak
  ho použít.
- Přesná formální kontrola z čísel vytažených z PDF (písmo, velikost, řez,
  barva, polohy), obsahová kontrola úsudkem modelu, kontrola zdrojů (`.tex`,
  log) tam, kde to pravidlo vyžaduje.
- Hlášení s ID pravidel, stranou, změřenou hodnotou a očekávanou hodnotou.

## Ne-cíle

- Práce psané ve Wordu (repo je jen pro LaTeX). *(potvrzeno uživatelem)*
- Opravy práce — skill nemění `.tex` ani jiné soubory práce. Pokud student
  opravu chce, požádá o ni zvlášť, mimo skill.
- Psaní obsahu (úvodu, závěru…) — mimo stupeň 2.
- Nové nebo změněné pravidlo — pravidla jsou jediný zdroj pravdy; skill je
  jen čte. Změna pravidla jde přes PR do `docs/pravidla/`.
- Kontrola odborné správnosti (funkčnost programu, správnost metod).

## Anti-cíle

- Skill, který „vymýšlí“ pravidla mimo `docs/pravidla/` nebo hodnotí bez
  odkazu na ID.
- Hlášení odhadnutých čísel jako změřených.
- Chyba hlášená tam, kde pravidlo připouští variantu nebo je jen doporučením
  (seminář) — to je upozornění, ne chyba.
- Načtení všech 212 pravidel a celého PDF do kontextu najednou.

## Přístup

**A) Skript vytáhne fakta z PDF, posoudí je Claude** — *zvoleno uživatelem.*

Zvažované varianty:
- **B) Celá kontrola jako skript** (každé měřitelné pravidlo naprogramované
  s prahy) — deterministické, ale ~150 kontrol duplikujících pravidla; každá
  změna pravidla = změna kódu. Zamítnuto.
- **C) Bez skriptu, Claude čte PDF jako obrázky** — bez závislostí, ale
  rozdíly v bodech a velikostech písma jen odhadem; formální pravidla by byla
  nepřesná. Zamítnuto (zůstává jako záložní režim, viz níže).

### Revize: kontrola částí subagenty *(schváleno uživatelem 2026-11-22)*

Původní postup procházel všechny části postupně v jednom kontextu; u dlouhé
práce by se kontext zaplnil a pozdější části by dostaly menší pozornost.
Uživatel navrhl rozdělit kontrolu mezi agenty. Zvoleno spojení obou přístupů:

- **Hlavní agent** sestaví mapu stran ze souhrnu, zjistí varianty a sám
  zkontroluje pravidla přes celou práci (záhlaví, číslování, okraje, pořadí
  částí, rozsah, log překladu) — ta potřebují vidět všechny strany najednou.
- **Subagenti `kontrola-casti`** (`.claude/agents/kontrola-casti.md`) běží
  souběžně, každý pro jednu skupinu stran se svými soubory pravidel
  a zjištěnými variantami: úvodní strany; obsah a seznamy; úvod a závěr
  (spolu, kvůli porovnání cílů); kapitoly po ≈ 15 stranách; literatura
  a citace; obrázky, tabulky a rovnice. Vracejí nálezy v pevném řádkovém
  formátu; nic nezapisují.
- **Sloučení:** hlavní agent spojí duplicity, porovná pozorování jednotnosti
  mezi skupinami a zapíše hlášení.
- Subagent má jen nástroje Read, Grep, Glob, Bash (bez Edit a Write, nemůže
  spouštět další agenty). Bash technicky zapisovat umí — zákaz zápisu je
  v jeho pokynech, ne vynucený.
- Režim **bez subagentů** zůstává (na žádost nebo bez nástroje Agent):
  skupiny projde hlavní agent postupně podle pokynů subagenta. Důvod:
  subagenti znovu načítají pravidla, celá kontrola spotřebuje víc tokenů.

Zvažované a zamítnuté: jen postupná kontrola (nestačí na dlouhou práci);
subagent pro každou stranu (pravidla stran spolu souvisí, mnohonásobná
spotřeba).

## Součásti

```
.claude/skills/kontrola-prace/
├── SKILL.md        ← postup kontroly pro Clauda (frontmatter name, description)
├── README.md       ← pro studenta: jak funguje, jak zprovoznit, jak použít
├── mereni.md       ← jak číst fakta z vytahni.py, závažnost (pro oba agenty)
├── vytahni.py      ← fakta z PDF (PyMuPDF)
├── pravidla.py     ← výběr pravidel z docs/pravidla (filtr podle souboru, ID, štítku)
├── test_vytahni.py ← testy na Dokumenty/Sablona.pdf
├── test_pravidla.py
└── test_skill.py   ← definice subagenta, cesty k pravidlům, pokrytí skupin
.claude/agents/
└── kontrola-casti.md ← subagent pro kontrolu jedné skupiny stran
```

### vytahni.py

Závislost: `pymupdf` (pip; Windows, macOS i Linux, bez dalších programů).
Pouze standardní knihovna + PyMuPDF.

- `python3 vytahni.py PDF --souhrn` → JSON: počet stran, rozměry stran,
  použitá písma (název, vložené ano/ne), záložky PDF (osnova z hyperref)
  s čísly stran, a pro každou stranu: první řádek textu pod záhlavím, text
  a poloha záhlaví a zápatí (číslo stránky), počet obrázků a tabulkových
  čar. Slouží k rozpoznání typů stránek (sekce Rozpoznání v pravidlech).
- `python3 vytahni.py PDF --strany 3-5` → JSON pro vybrané strany: řádky textu
  (text, bbox), úseky (text, písmo, velikost, tučně, kurzíva, barva),
  **pásy inkoustu** (horní/dolní hrana, x od–do v pt; stejná metoda jako při
  měření Word PDF: vykreslení 288 dpi v odstínech šedi, práh 200, mezera 3 px —
  hodnoty v pravidlech jsou měřené takto), obrázky (bbox, rozměry v px),
  čáry a obdélníky (bbox), poznámka o přetečení textu za okraje.
- `python3 vytahni.py PDF --text 10-12` → prostý text stran (pro obsahová
  pravidla).
- Jednotky pt, počátek levý horní roh, strany číslované fyzicky od 1.

### pravidla.py

Tenká obálka nad `docs/pravidla/kontrola.py` (`nacti_pravidla`), žádná
duplikace rozboru.

- `--soubor stranky/uvod.md` → pravidla daného souboru (Markdown, jak jsou).
- `--id CIT-F01,DOK-F09` → jen tato pravidla.
- `--stitek měření` → pravidla se štítkem.
- `--prehled` → tabulka ID | název | štítky „jak“ pro všechny soubory
  (orientace bez načítání textu).

### SKILL.md — postup

1. **PDF:** argument, jinak nejnovější z `output/prace_*.pdf` (lokální
   `./build.sh`) a `output/prace.pdf`, jinak nejnovější `Verze/prace_*.pdf`
   (CI). Log překladu: `output/logs/build.log` (výstup latexmk včetně
   varování Overfull / undefined); když chybí, pravidla vyžadující log se
   přeskočí s poznámkou. Je-li některý `.tex` v `src/` novější než PDF,
   upozorní a nabídne sestavení (`./build.sh`); bez souhlasu nesestavuje.
2. **Závislosti:** ověří `import pymupdf`; když chybí, nabídne
   `pip install pymupdf`, a když to nejde, pokračuje v záložním režimu
   (stránky jako obrázky, formální měření označí jako „odhad“).
3. **Souhrn** (`--souhrn`) → přiřazení fyzických stran k typům podle sekcí
   Rozpoznání (titulní 1, zadání 2, abstrakt 3, prohlášení 4, poděkování 5,
   dál podle nadpisů 1. úrovně a záložek PDF).
4. **Volba variant:** z práce zjistí, kterou variantu používá u pravidel
   s Variantami (číslování od Obsahu / od Úvodu, citační systém
   harvard / APA, dělení slov…), a dál ji drží jednotně; použité varianty
   vypíše v hlášení.
5. **Po částech** (subagenti, viz Revize výše): pro každou skupinu stran načte pravidla
   (`pravidla.py --soubor …` + `dokument.md`), fakta jen pro jeho strany
   a vyhodnotí. Měřitelná pravidla podle čísel z `vytahni.py` (tolerance
   z pole Ověření), textová podle textu, „posouzení“ úsudkem, „zdrojový-soubor“
   v `src/**/*.tex` a v `output/logs/build.log`, `latex-chyby.md` v celé práci.
6. **Nepopsané prvky** (seznam v `docs/pravidla/README.md`): zmíní, že je
   našel, a že k nim nemá pravidlo — nehodnotí.
7. **Rozsah práce** (DOK-F20): vždy změří a uvede.
8. **Hlášení:** soubor `output/kontrola_<RRRR-MM-DD_HHMM>.md` (adresář
   `output/` je v `.gitignore`) a krátké shrnutí v konverzaci.

Režimy podle argumentu: celá práce (výchozí), jedna část („úvod“, „citace“,
„titulní strana“ → odpovídající soubory pravidel), jen formální / jen obsahová
(podle F/O v ID).

### Hlášení

```markdown
# Kontrola práce — <název z titulní strany>, <datum>
PDF: output/prace.pdf (42 stran) · režim: celá práce · varianty: číslování od Obsahu (DOK-F09 a), citace harvard (CIT-F01 a)

## Souhrn
3 chyby · 7 upozornění · 2 poznámky · rozsah: Úvod–Závěr 31 stran, 9 120 slov, 38,4 normostrany

## Chyby
- **NA1-F04** s. 11 — nadpis „1 Teoretická část“ začíná 98,2 pt od horní hrany, očekáváno ≈ 75,8 pt (±2).
...
## Upozornění
- **ZAV-O09** (doporučení semináře) s. 40–43 — závěr má 3,5 strany; doporučeno ≤ 2 / 2–3 strany.
## Poznámky a nepopsané prvky
- s. 27 výpis zdrojového kódu — pro jeho formát pravidlo není.
## Zkontrolováno bez nálezu
NA1-F01, NA1-F02, … (seznam ID)
```

Závažnost:
- **chyba** — porušené pravidlo bez varianty, nebo neodpovídá žádné variantě;
- **upozornění** — pravidlo, jehož jediným zdrojem je `seminář …`,
  „doporučení“ v textu pravidla, nebo výsledek „posouzení“;
- **poznámka** — míchání variant, nepopsané prvky, informace (rozsah).

Každý nález uvádí ID, stranu, změřenou / nalezenou hodnotu a očekávanou
hodnotu nebo citaci pravidla. Odhad (záložní režim, posouzení) je tak
označen.

### README.md (u skillu)

Krátké, tři části:
- **Jak funguje** — 3–4 věty (skript vytáhne fakta, Claude porovná s pravidly
  v `docs/pravidla/`, hlášení do `output/`), stupeň 2 podle MP 8/2026,
  skill nic nepřepisuje.
- **Jak ho přidat** — fork repa, Claude Code v kořeni repa (skill se načte
  sám), `pip install pymupdf` (případně ve venv).
- **Jak ho použít** — sestavit PDF (`./build.sh` nebo stáhnout z `Verze/`),
  v Claude Code napsat např. „zkontroluj práci“ / `/kontrola-prace`,
  „zkontroluj jen úvod“; kde najít hlášení; upozornění na osobní a důvěrné
  údaje (MP 8/2026 čl. 3).

Odkaz na skill přibude do kořenového `README.md` (struktura repa) a do
`docs/README.md`.

## Testy

- `test_vytahni.py` (pytest) na `Dokumenty/Sablona.pdf` — známé hodnoty
  z měření při tvorbě pravidel:
  - s. 1 pásy inkoustu: první 96,5 pt, název práce 360,2 pt (±0,5);
  - s. 6: záhlaví 38,5–48,0 pt, x 250–402;
  - s. 10: číslo stránky inkoust 796,5–803,8, pravá hrana ≈ 523,5;
  - souhrn: 17 stran, A4; písma obsahují Calibri a Calibri Light;
  - úseky: nadpis „Abstrakt“ s. 3 velikost 18 pt;
  - `--text 15` obsahuje „Závěr“.
- `pravidla.py`: `--id CIT-F01` vrátí právě to pravidlo; `--soubor
  stranky/uvod.md` obsahuje UVO-F01; `--stitek měření` nevrátí pravidlo bez
  štítku měření.
- Ruční ověření: skill spuštěný na aktuálním PDF šablony (`Verze/`)
  vytvoří hlášení; zkontrolovat, že nálezy odpovídají známým odchylkám
  (např. záhlaví na středu místo tabulátoru — DOK-F08).

## Omezení a rozhodnutí *(schváleno s návrhem)*

- Hlášení do `output/` (už gitignorováno), ne do repa — práce studenta se
  nezanáší soubory skillu.
- Skill bez souhlasu nesestavuje PDF ani neinstaluje balíčky — nabídne příkaz.
- Výsledky „posouzení“ se mezi běhy mohou lišit; proto jsou vždy jen
  upozornění.
- Přístup k datům: text práce se při kontrole zpracovává modelem; README
  upozorní, ať student do práce v době kontroly nedává osobní a důvěrné údaje,
  případně je anonymizuje (MP 8/2026 čl. 3 odst. 1 písm. c).
- Testy se spouštějí ručně (`python3 -m pytest .claude/skills/kontrola-prace`),
  CI se nemění.

## Co je ponecháno na tom, kdo staví

- Přesná struktura JSON z `vytahni.py` (názvy klíčů), pokud ji SKILL.md
  popisuje.
- Formulace SKILL.md (musí být stručná — načítá se do kontextu).
- Rozdělení postupu do kroků a pořadí částí.
