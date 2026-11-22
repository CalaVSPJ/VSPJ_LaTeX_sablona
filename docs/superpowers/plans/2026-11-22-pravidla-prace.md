# Popis pravidel závěrečné práce VŠPJ — plán

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sepsat v `docs/pravidla/` popisy formálních (a známých obsahových) pravidel pro každý typ stránky a prvku závěrečné práce VŠPJ, se zdroji a variantami.

**Architecture:** Jeden Markdown soubor na typ v pevném formátu (pravidlo = nadpis `### ID Název` + pevná pole). Malý kontrolní skript `docs/pravidla/kontrola.py` hlídá formát, jedinečnost ID, platnost odkazů na zdroje a pokrytí zdrojů; slouží jako „test“ každého úkolu. Fakta ze zdrojů (styly, oddíly, pokyny, měření Word PDF) se nejdřív vytáhnou do pracovních souborů, z nich se pak píše.

**Tech Stack:** Markdown, Python 3 (jen standardní knihovna) + pytest, `pdftoppm`/`pdftotext` (poppler), PIL pro měření.

**Spec:** `docs/superpowers/specs/2026-11-22-pravidla-prace-design.md`

## Global Constraints

- Jazyk všech popisů: čeština. Hodnoty v bodech s jednotkou „pt“; desetinná čárka.
- Převody: twips / 20 = pt; `w:sz` / 2 = pt; `w:line="276"` (lineRule auto) = řádkování 1,15.
- ID: `PREFIX-NN`; formální 01–19, obsahová 20–99; ID se nepřečíslovávají ani znovu nepoužijí.
- Pole pravidla v tomto pořadí: `- Pravidlo:`, `- Zdroj:`, `- Varianty:`, `- Ověření:`, volitelně `- Poznámka:`.
- Tvary zdroje: `příručka <kap>` (např. `příručka 6.2`), `šablona <styl|oddíl N|místo>`, `Word PDF s. N` (N = fyzická strana PDF od 1, ne tištěné číslo; změřené hodnoty s `(změřeno)`), odkaz `viz PREFIX-NN`.
- Rozpor = varianty, každá se zdrojem; nikdy tiše nevybírat jednu.
- LaTeX šablona ani její PDF nejsou zdroj pravidel. LibreOffice export se nepoužívá.
- Rozsah: bakalářská a diplomová práce v češtině; seminární práce mimo rozsah.
- Písmo: Calibri / Calibri Light, varianta Carlito jako přijatelná náhrada (Calibri není volně šiřitelné).
- Pravidla nesmí záviset na konkrétním textu ze šablony („Jan Nový“, „Vlastní text…“); pevné texty (nadpisy, „Bakalářská práce“) ano.
- Aktuální verze zdrojů (pro obnovu): https://kts.vspj.cz/cs/statni-zaverecne-zkousky/zaverecne-prace a https://is.vspj.cz/dokumentace-student/.
- Zdroje: příručka = `Dokumenty/Jak psát práce na VŠPJ.pdf` (text shodný s DOCX od uživatele); šablona = `Dokumenty/Sablona.docx`; Word PDF = `Dokumenty/Sablona.pdf` (17 stran).
- Commity jen lokálně na větev `pravidla-prace`; push a PR až po souhlasu uživatele.

Mapa Word PDF (fyzické strany): 1 titulní, 2 zadání, 3 abstrakt, 4 prohlášení, 5 poděkování, 6 obsah, 7 seznam obrázků, 8 seznam tabulek, 9 seznam zkratek, 10 úvod, 11–12 kapitola 1 (Nadpis 1–3), 13 kapitola 2 (obrázek, tabulka), 14 rovnice a výčty, 15 závěr, 16 literatura, 17 přílohy.

## Review Focus

1. **Špatně převedená hodnota z DOCX** (twips × půlbody, zděděná mezera za odstavcem ze stylu Normální) — u každého stylového pravidla musí hodnota sedět s `fakta/styly.md`; Task 2 obsahuje kontrolní hodnoty, úkoly 3–9 krok „porovnat s fakty“.
2. **Tiše vybraná varianta** — každý rozpor z tabulky ve specifikaci musí skončit u pravidla s neprázdnými Variantami; vynucuje `kontrola.py --uplne` (test `test_rozpor_bez_variant`).
3. **Pravidlo vázané na vzorový text** — `kontrola.py` odmítne „Jan Nový“, „Starý“, „Vlastní text“ v poli Pravidlo (test `test_vzorovy_text`).
4. **Chybná strana Word PDF** (tištěné číslo místo fyzické strany) — `kontrola.py` odmítne `Word PDF s. N` mimo 1–17 (test `test_strana_mimo_rozsah`); úkoly používají mapu výše.
5. **Stejné pravidlo ve dvou souborech s jinou hodnotou** — obecné pravidlo je jen v `dokument.md`, ostatní píšou `viz DOK-NN`; `kontrola.py` ověří existenci odkazů (test `test_neznamy_odkaz`), úkoly mají krok „nezdvojovat pravidla z DOK“.

---

### Task 1: Kontrolní skript a README

**Files:**
- Create: `docs/pravidla/kontrola.py`
- Create: `docs/pravidla/test_kontrola.py`
- Create: `docs/pravidla/README.md`
- Add (commit): `docs/superpowers/specs/2026-11-22-pravidla-prace-design.md`, `docs/superpowers/plans/2026-11-22-pravidla-prace.md`

**Interfaces:**
- Produces:
  - `PREFIXY: dict[str, str]` — relativní cesta → prefix: `dokument.md`→`DOK`; `stranky/{titulni-strana,zadani,abstrakt,prohlaseni,podekovani,obsah,seznam-obrazku,seznam-tabulek,seznam-zkratek,uvod,kapitola,zaver,seznam-literatury,prilohy}.md`→`TIT,ZAD,ABS,PRO,POD,OBS,SOB,STA,SZK,UVO,KAP,ZAV,LIT,PRI`; `prvky/{nadpis-1,nadpis-2,nadpis-3,obrazek,tabulka,rovnice,vycet-seznam,odkaz-v-textu,poznamka-pod-carou,polozka-literatury}.md`→`NA1,NA2,NA3,OBR,TAB,ROV,VYC,CIT,PPC,BIB`.
  - `KAPITOLY_PRIRUCKY: list[str]` = `1, 1.1, 1.2, 1.3, 2, 3, 4, 4.1–4.5, 5, 5.1–5.3, 6, 6.1–6.3, 7, 7.1–7.3, 8, 9, 10, 11, 11.1, 11.2, 12, 13`.
  - `STYLY_SABLONY: list[str]` = `Normální, Nadpis 1, Nadpis 2, Nadpis 3, Název, Titulek, Zdroj, Tabulka, Seznam literatury, Obsah 1, Obsah 2, Text poznámky pod čarou`.
  - `@dataclass Pravidlo(id: str, nazev: str, kategorie: Literal["formalni","obsahova"], pole: dict[str, str], soubor: Path, radek: int)`
  - `nacti_pravidla(koren: Path) -> list[Pravidlo]`
  - `zkontroluj(koren: Path, uplne: bool = False) -> list[str]` — chyby ve tvaru `soubor:řádek: zpráva`
  - CLI: `python3 docs/pravidla/kontrola.py [--uplne] [koren=docs/pravidla]` → exit 0 a `OK: <N> pravidel v <M> souborech`, jinak chyby a exit 1.

- [ ] **Step 1: Napsat testy** v `docs/pravidla/test_kontrola.py` (pytest, soubory v `tmp_path`). Pomocná funkce `soubor(tmp_path, cesta, text)`. Platný vzor = soubor `prvky/obrazek.md` s `# Obrázek`, `## Formální`, pravidlem `### OBR-01 …` se všemi poli (`Zdroj: šablona styl Titulek; příručka 6.2`, `Varianty: —`, `Ověření: PDF — …`) a `## Obsahová`. Testy:
  - `test_platny_soubor` → `zkontroluj(...) == []`
  - `test_spatny_prefix` (`### TAB-01` v `obrazek.md`) → chyba obsahuje `prefix`
  - `test_duplicitni_id` (OBR-01 dvakrát) → `duplicitní`
  - `test_formalni_cislo_mimo_rozsah` (`OBR-20` pod Formální) a `test_obsahove_cislo_mimo_rozsah` (`OBR-05` pod Obsahová)
  - `test_chybi_pole` (bez `- Ověření:`) → `Ověření`
  - `test_spatne_poradi_poli`
  - `test_neplatny_zdroj` (`Zdroj: internet`) → `zdroj`
  - `test_neplatna_kapitola` (`příručka 14`) a `test_strana_mimo_rozsah` (`Word PDF s. 18`)
  - `test_varianty_jedna_polozka` (jediná `  - a) …`) → `aspoň dvě`
  - `test_varianta_bez_zdroje` (`  - a) vlevo` bez ` — zdroj`)
  - `test_neplatne_overeni` (`Ověření: oko`)
  - `test_vzorovy_text` (`Jan Nový` v Pravidlu)
  - `test_chybi_sekce_obsahova`
  - `test_neznamy_odkaz` (`viz DOK-07`, DOK-07 neexistuje) → chyba jen s `uplne=True`
  - `test_rozpor_bez_variant` (README tabulka rozporů odkazuje OBR-01, které má `Varianty: —`, `uplne=True`)
  - `test_pokryti_chybi_kapitola` (`pokryti.md` bez řádku `příručka 6.2`, `uplne=True`)
  - `test_chybi_soubor_typu` (`uplne=True`, chybí `prvky/tabulka.md`)

- [ ] **Step 2: Spustit** `cd docs/pravidla && python3 -m pytest -q` → FAIL (`ModuleNotFoundError: kontrola`).

- [ ] **Step 3: Napsat `kontrola.py`** s rozhraním výše. Rozbor po řádcích (regexy, žádné závislosti). Pravidla rozboru:
  - Varianty: buď `—`, nebo prázdný text za dvojtečkou a ≥ 2 podřádky `  - <písmeno>) <text> — <zdroj>[; <zdroj>]`.
  - Ověření začíná `PDF`, `zdroj` nebo `PDF + zdroj`, pak ` — ` a text.
  - Zdroj se dělí `;`; každá část odpovídá jednomu z tvarů v Global Constraints; `příručka` smí mít víc kapitol oddělených čárkou, každá z `KAPITOLY_PRIRUCKY`.
  - Odkazy `[A-Z0-9]{3}-\d{2}` kdekoli v polích se ověřují jen při `uplne`.
  - V `uplne` navíc: všechny soubory z `PREFIXY` existují; tabulka `## Rozpory` v README (sloupec `Pravidla` s ID) → každé ID existuje a má Varianty ≠ `—`; `pokryti.md` obsahuje řádek pro každou položku `KAPITOLY_PRIRUCKY` (tvar `příručka X`), `STYLY_SABLONY` (tvar `šablona styl X`) a `šablona oddíl 1`–`7`, každý s ID nebo textem `vynecháno: <důvod>`.
  - README.md, pokryti.md, kontrola.py a test se nekontrolují jako soubory typů.

- [ ] **Step 4: Spustit** `cd docs/pravidla && python3 -m pytest -q` → všechny PASS.

- [ ] **Step 5: Napsat `docs/pravidla/README.md`**: účel (podklad pro kontrolní skill, čitelný pro lidi), zdroje (tři, s cestami a pravidlem pro Word PDF stránky), sekci `## Kde získat aktuální zdroje` s odkazy https://kts.vspj.cz/cs/statni-zaverecne-zkousky/zaverecne-prace a https://is.vspj.cz/dokumentace-student/ (příručka i šablona; při nové verzi aktualizovat `Dokumenty/` a projít pravidla), seznam souborů s prefixy, formát pravidla (vzor ze specifikace), zásady pro varianty („vyhovuje kterákoli varianta“), převody jednotek, jak spustit `kontrola.py`, a prázdnou tabulku `## Rozpory` se sloupci `Téma | Příručka | Šablona DOCX / Word PDF | Pravidla` (řádky ze specifikace, sloupec Pravidla zatím prázdný — vyplní Task 10).

- [ ] **Step 6: Ověřit** `python3 docs/pravidla/kontrola.py` → `OK: 0 pravidel v 0 souborech`.

- [ ] **Step 7: Commit** spec, plán, `kontrola.py`, test, README — `docs: formát popisů pravidel a kontrolní skript`.

### Task 2: Fakta ze zdrojů (pracovní, mimo repo)

**Files:**
- Create: `$S/fakta/styly.md`, `$S/fakta/oddily.md`, `$S/fakta/pokyny.md`, `$S/fakta/mereni.md` kde `$S` = pracovní složka mimo repo
- Use: `$S/docx_sections.py`, `$S/ink.py` (`bands(pdf, page, dpi=288, thr=200, gap=3) -> list[(top, bottom, xmin, xmax)]` v pt), `$S/pages.py`

**Interfaces:**
- Produces: čtyři soubory faktů, ze kterých úkoly 3–9 berou hodnoty (vždy s uvedením zdroje).

- [ ] **Step 1: `styly.md`** — pro každý styl z `STYLY_SABLONY` tabulka: písmo (theme major = Calibri Light, minor = Calibri), velikost, tučné/kurzíva, zarovnání, mezera před/za, řádkování, odsazení/předsazení, keepNext, pageBreakBefore, barva — **s rozvinutou dědičností** z `basedOn` a `docDefaults`. Kontrolní hodnoty, které musí vyjít: Normální 11 pt, za 6 pt, 1,15, do bloku; Nadpis 1 18 pt tučně, před 18 pt, za 6 pt, vlevo, předsazení 21,55 pt; Nadpis 2 15 pt, předsazení 28,9 pt; Nadpis 3 12 pt; Titulek 10 pt tučně na střed, za 0; Zdroj 10 pt kurzíva na střed, za 6 pt; Tabulka 10 pt, vlevo, za 0, řádkování 1; Seznam literatury předsazení 17,85 pt, vlevo; Obsah 2 odsazení 11,05 pt. Pokud cokoli nesedí, zastavit a nahlásit.
- [ ] **Step 2: `oddily.md`** — 7 oddílů: rozsah (první/poslední nadpis), okraje, záhlaví/zápatí (text, zarovnání, barva), pole PAGE, `pgNumType`, `vAlign`. Kontrola: okraje 2,5/2,5/3,5 vlevo/2,5 vpravo cm; PAGE jen v oddílu 6; oddíl 3 `vAlign=bottom`; záhlaví „Vysoká škola polytechnická Jihlava“ šedé (#808080) kurzívou.
- [ ] **Step 3: `pokyny.md`** — všechny pokyny šablony (modré/vysvětlující texty, rozbalovací pole „Zvolte položku“), každý se stranou Word PDF. Mezi nimi musí být: abstrakt max. 150 slov; 3–7 klíčových slov oddělených středníkem; obsah jen 2 úrovně; seznamy od 5 položek; úvod (cíl, motivace, aktuálnost); závěr (výčet ze šablony); kapitola na novém listě; max. 3 úrovně nadpisů; výčet ne hned za nadpisem; přílohy (výčet, označení A.1, každá na nové stránce).
- [ ] **Step 4: `mereni.md`** — z Word PDF pomocí `ink.py`: pro strany 1–17 horní hrana a levý/pravý okraj inkoustu prvního nadpisu, poloha záhlaví a čísla stránky (x vpravo, y od spodu), na straně 1 horní hrany řádků (škola, program, název, typ, autor, vedoucí, město a rok), na straně 13 vzdálenosti obrázek→titulek→zdroj a titulek→tabulka→zdroj, na straně 14 odsazení odrážek a poloha čísla rovnice. Kontrola: titulní strana škola ≈ 96,5 pt, název ≈ 360,2 pt od horního okraje papíru (±0,5).
- [ ] **Step 5: Ověřit** — každý soubor má u každé hodnoty zdroj; kontrolní hodnoty z kroků 1–4 sedí. Bez commitu (mimo repo).

### Task 3: Celý dokument (`dokument.md`)

**Files:** Create `docs/pravidla/dokument.md`
**Interfaces:** Consumes fakta (Task 2), formát (Task 1). Produces ID `DOK-NN`, na která odkazují všechny další soubory.

- [ ] **Step 1: Napsat formální pravidla** pokrývající: formát A4 a okraje (příručka 10, šablona oddíly); písmo základní a nadpisové + varianta Carlito (příručka 2, 3); odstavec Normální (zarovnání do bloku, 11 pt, 1,15, za 6 pt, bez odsazení prvního řádku; příručka 1.1, 1.2, 3); žádné prázdné odstavce k odsazení (příručka 1); sirotci a vdovy (1.3); záhlaví (šablona oddíly 4–7); **číslování stránek** — počítají se od titulní, zobrazují se od Obsahu (příručka 12) × od Úvodu (šablona oddíl 6) jako varianty, poloha vpravo dole (příručka 12, Word PDF změřeno); dělení slov (příručka 4.5 × šablona bez auto-dělení → varianty); jednopísmenné předložky a pevné mezery (4, 4.5); zvýrazňování — kurzíva, žádné podtržení, tučné (příručka 2 × šablona Úvod → varianty), žádná barva; uvozovky, pomlčky, spojovník, trojtečka (4.1–4.4); čísla, jednotky, data, telefon (4.5); max. 3 úrovně nadpisů (příručka 3, šablona); kapitola 1. úrovně na nové stránce (šablona); pořadí povinných částí (titulní → … → přílohy dle šablony).
- [ ] **Step 2: Obsahová sekce** — jen to, co zdroje výslovně říkají (např. zkratky bez seznamu zkratek se při prvním použití rozepíšou — příručka 4.5); jinak „k doplnění“.
- [ ] **Step 3: Porovnat** každou hodnotu s `fakta/` a s textem příručky.
- [ ] **Step 4: Ověřit** `python3 docs/pravidla/kontrola.py` → `OK`.
- [ ] **Step 5: Commit** — `docs(pravidla): celý dokument`.

### Task 4: Nadpisy (`prvky/nadpis-1.md`, `nadpis-2.md`, `nadpis-3.md`)

**Files:** Create tři soubory v `docs/pravidla/prvky/`
**Interfaces:** Consumes `DOK-*` (písmo, nová stránka). Produces `NA1-*`, `NA2-*`, `NA3-*`.

- [ ] **Step 1:** Pro každou úroveň: písmo/velikost/řez, zarovnání (u Nadpisu 1 varianty: na střed — příručka 3 (Tab. 1) × vlevo — šablona styl Nadpis 1; Word PDF s. 11), mezery před/za (a že Word mezeru před na začátku stránky vynechává, u prvního nadpisu oddílu ne — Word PDF změřeno), číslování desetinné bez tečky za posledním číslem (příručka 4.1, 5.1), předsazení čísla, tečka za nadpisem se nepíše (4.1), svázat s následujícím, nečíslované nadpisy stylu Název (šablona styl Název, příručka 3). Obsahová: první věta za nadpisem není jeho pokračováním; mezi nadpisy různých úrovní aspoň jeden odstavec (příručka 3). Pravidla z DOK nezdvojovat — odkázat `viz DOK-NN`.
- [ ] **Step 2: Porovnat** s `fakta/styly.md` a `fakta/mereni.md`.
- [ ] **Step 3: Ověřit** `kontrola.py` → `OK`. **Step 4: Commit** — `docs(pravidla): nadpisy`.

### Task 5: Obrázek, tabulka, rovnice

**Files:** Create `docs/pravidla/prvky/obrazek.md`, `tabulka.md`, `rovnice.md`
**Interfaces:** Consumes `DOK-*`, `NA1-*`. Produces `OBR-*`, `TAB-*`, `ROV-*`.

- [ ] **Step 1:** Obrázek: na střed, titulek pod obrázkem (Titulek), zdroj pod titulkem (Zdroj) s variantou „zdroj:“ (příručka 6.2) × „Zdroj:“ (šablona), formát „Obr. N: popis“ bez tečky, číslování průběžné v celé práci, bez dělení slov v titulku, poměr stran zachován, šířka nejvýš šíře textu, graf = „Obr.“, vlastní zdroj „vlastní zpracování“ / „vlastní fotografie + rok“ (příručka 6.2), změřené mezery (Word PDF s. 13). Tabulka: titulek nad tabulkou, zdroj pod, na střed, text v tabulce s variantami (příručka 3, 6.1: 11/10 pt na střed × šablona styl Tabulka: 10 pt vlevo), řádkování 1 bez mezer, celá tabulka s titulkem a zdrojem na jedné stránce (6.1), jednotný vzhled tabulek. Rovnice: na samostatném řádku na střed, číslo „(N)“ zarovnané vpravo, proměnné kurzívou (příručka 9, šablona). Obsahová: kapitola nezačíná obrázkem/tabulkou (6); proměnné rovnice vysvětlené (9); zdroj uveden vždy (6.1, 6.2).
- [ ] **Step 2–4:** porovnat s fakty; `kontrola.py` → `OK`; commit — `docs(pravidla): obrázek, tabulka, rovnice`.

### Task 6: Výčet, odkaz v textu, poznámka pod čarou, položka literatury

**Files:** Create `docs/pravidla/prvky/vycet-seznam.md`, `odkaz-v-textu.md`, `poznamka-pod-carou.md`, `polozka-literatury.md`
**Interfaces:** Consumes `DOK-*`. Produces `VYC-*`, `CIT-*`, `PPC-*`, `BIB-*`.

- [ ] **Step 1:** Výčet: písmo a řádkování jako text, mezera za jen po poslední položce, jednotné odrážky v celé práci, číslování „1.“ / „a)“ zarovnané zprava, odsazení (Word PDF s. 14 změřeno), interpunkce nevětných/větných položek (příručka 5, 5.2, šablona). Odkaz v textu: harvardský styl „(Autor, rok)“ / „Autor (rok, s. N)“, „a kol.“ od 4 autorů, a/b u stejného roku, žádné číselné odkazy ani poznámky pod čarou pro zdroje (příručka 7.3, šablona Citace). Poznámka pod čarou: menší stupeň stejného písma (šablona styl Text poznámky pod čarou: 10 pt, řádkování 1, za 0), značka těsně za slovem (příručka 8). Položka literatury: styl Seznam literatury (předsazení, vlevo; varianta názvu stylu „Bibliografie“ — příručka 3 × šablona), ČSN ISO 690, abecedně (7.1, 7.2). Obsahová: přímé citace max. 10 % (7.3), poznámky ne pro citace (8), výčet ne hned za nadpisem (5.2), celý výčet pokud možno na jedné stránce (5.2).
- [ ] **Step 2–4:** porovnat; `kontrola.py` → `OK`; commit — `docs(pravidla): výčty, citace, poznámky, literatura`.

### Task 7: Úvodní stránky (titulní, zadání, abstrakt, prohlášení, poděkování)

**Files:** Create `docs/pravidla/stranky/titulni-strana.md`, `zadani.md`, `abstrakt.md`, `prohlaseni.md`, `podekovani.md`
**Interfaces:** Consumes `DOK-*`, `NA1-*`. Produces `TIT-*`, `ZAD-*`, `ABS-*`, `PRO-*`, `POD-*`.

- [ ] **Step 1:** Titulní strana: obsah řádků (škola verzálkami, program, název verzálkami, „Bakalářská práce“/„Diplomová práce“, autor, vedoucí s tituly, místo a rok — příručka 11.1, šablona), písmo/velikost/řez/zarovnání každého řádku (šablona přímé formátování), **polohy** horních hran z `fakta/mereni.md` (Word PDF s. 1 (změřeno)), dlouhý název zalomen na střed, bez záhlaví a čísla. Zadání: samostatná strana, vkládá se list z IS. Abstrakt: nadpisy Abstrakt / Klíčová slova / Abstract / Keywords stylem Název (mezery z Word PDF s. 3), jedna strana. Prohlášení: znění dle šablony, místo a datum, tečkovaná linka a „Podpis studenta/ky“ vpravo, poloha z Word PDF s. 4. Poděkování: nadpis stylem Název, řez a zarovnání textu přesně podle DOCX, **svislá poloha** dole na stránce (šablona oddíl 3 vAlign=bottom, Word PDF s. 5) — bez varianty, v Poznámce uvést, že LibreOffice ji vykreslí nahoře (LibreOffice není zdroj). Všechny úvodní strany: počítají se, nečíslují se, bez záhlaví (viz DOK). Obsahová: abstrakt max. 150 slov, 3–7 klíčových slov oddělených středníkem, anglický překlad obou (šablona); poděkování nepovinné (šablona „můžete“).
- [ ] **Step 2–4:** porovnat (řez textu poděkování ověřit v DOCX, ne odhadovat); `kontrola.py` → `OK`; commit — `docs(pravidla): úvodní stránky`.

### Task 8: Obsah a seznamy

**Files:** Create `docs/pravidla/stranky/obsah.md`, `seznam-obrazku.md`, `seznam-tabulek.md`, `seznam-zkratek.md`
**Interfaces:** Consumes `DOK-*`, `NA1-*`, `OBR-*`, `TAB-*`. Produces `OBS-*`, `SOB-*`, `STA-*`, `SZK-*`.

- [ ] **Step 1:** Obsah: nadpis stylem Název na nové stránce, položky Obsah 1 (tučně, za 0) a Obsah 2 (odsazení, za 0), tečkovaný vodicí znak a číslo vpravo, první číslovaná strana (viz DOK). Seznam obrázků/tabulek: každý na nové stránce za obsahem (nebo před literaturou — příručka 6.3 → varianty umístění), položka „Obr. N: popis … strana“ bez odsazení. Seznam zkratek: samostatná stránka, zkratka a vysvětlení zarovnané tabulátorem (změřit Word PDF s. 9), mezera za položkou (šablona). Obsahová: obsah jen 2 úrovně, bez sebe sama a úvodních stran, zahrnuje seznamy a přílohy (šablona, příručka 5.3); seznamy jen od 5 položek (příručka 6.3, šablona); zkratky jen neběžné (šablona).
- [ ] **Step 2–4:** porovnat; `kontrola.py` → `OK`; commit — `docs(pravidla): obsah a seznamy`.

### Task 9: Úvod, kapitola, závěr, literatura, přílohy

**Files:** Create `docs/pravidla/stranky/uvod.md`, `kapitola.md`, `zaver.md`, `seznam-literatury.md`, `prilohy.md`
**Interfaces:** Consumes vše výše. Produces `UVO-*`, `KAP-*`, `ZAV-*`, `LIT-*`, `PRI-*`.

- [ ] **Step 1:** Úvod a závěr: nečíslovaný nadpis 1. úrovně, nová stránka, v obsahu (viz NA1, OBS). Kapitola: číslovaná, začíná odstavcem textu (ne obrázkem/výčtem). Seznam literatury: nečíslovaný nadpis jako Nadpis 1 (příručka 7.1), položky viz BIB, za poslední kapitolou. Přílohy: úvodní strana „Přílohy“, každá příloha na nové stránce (příručka 13, šablona), **označení** varianty „Příloha 1“ (příručka 13) × „Příloha A.1“ (šablona), **číslování stránek** varianty nečíslují se (příručka 13) × „nemusí se číslovat v návaznosti“ (šablona), seznam příloh pokud jich je víc (13). Obsahová: úvod (cíl, motivace, aktuálnost — šablona), závěr (výčet ze šablony), na každou přílohu odkaz v textu (13), převzaté přílohy se zdrojem (šablona), každá položka literatury citovaná v textu (7.1).
- [ ] **Step 2–4:** porovnat; `kontrola.py` → `OK`; commit — `docs(pravidla): úvod, kapitoly, závěr, literatura, přílohy`.

### Task 10: Rozpory a pokrytí

**Files:** Modify `docs/pravidla/README.md` (sloupec Pravidla v `## Rozpory`); Create `docs/pravidla/pokryti.md`

- [ ] **Step 1:** Vyplnit sloupec Pravidla u všech 10 rozporů ze specifikace (+ rozpory nalezené během úkolů 3–9, + varianta Carlito).
- [ ] **Step 2:** `pokryti.md` — tabulka `Zdroj | Pravidla` s řádkem pro každou kapitolu příručky, každý styl, každý oddíl a každý pokyn z `fakta/pokyny.md`; nepokryté s `vynecháno: <důvod>` (např. `příručka 11.2` — seminární práce mimo rozsah; `příručka 5.1` víceúrovňové římské číslování — práce používá desetinné).
- [ ] **Step 3: Ověřit** `python3 docs/pravidla/kontrola.py --uplne` → `OK: <N> pravidel v 25 souborech`; `python3 -m pytest -q docs/pravidla` → PASS.
- [ ] **Step 4: Ruční průchod** Word PDF strana po straně: každý viditelný formální znak (písmo, poloha, mezera) má pravidlo; doplnit chybějící.
- [ ] **Step 5: Commit** — `docs(pravidla): rozpory a pokrytí`. Push a PR jen po souhlasu uživatele.
