# Obsahová pravidla — plán

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Doplnit do `docs/pravidla/` obsahová pravidla („je úvod napsaný jako úvod?“) a citační varianty APA podle materiálů semináře SBP a Směrnice SP 2/2020.

**Architecture:** Stávající formát pravidel (ID `XXX-Onn`, pole, štítky). `kontrola.py` dostane nové tvary zdroje a kontrolu pokrytí kritérií posudku a materiálů semináře; ostatní úkoly jsou psaní pravidel ověřované `kontrola.py`.

**Tech Stack:** Markdown, Python 3 + pytest.

**Spec:** `docs/superpowers/specs/2026-11-22-obsahova-pravidla-design.md` (navazuje na `2026-11-22-pravidla-prace-design.md`)

## Global Constraints

- Čeština; ID `XXX-Onn` (obsahová) / `XXX-Fnn` (formální); ID se nepřečíslovávají ani znovu nepoužijí.
- Obsahová sekce začíná odstavcem `Účel: …` (volný text před prvním pravidlem).
- Obsahové pravidlo má ve Štítcích `obsah-textu` (nebo `styl` / `citace`) a aspoň jeden štítek „jak“; Ověření `PDF — <signály v textu>`.
- Nové tvary zdroje: `směrnice SP 2/2020` (+ volitelně `(čl. N)` / `(příloha 1)`), `seminář <téma>` s tématy přesně: Úvod, Závěr, Abstrakt, Typy BP, Rešerše, Citace, Typografie, Chyby, Vyhledávání; `APA manuál`.
- APA je **rovnocenná** varianta citací (bez výhrady); z APA manuálu jen citace v textu a seznam literatury, nic o obrázcích a tabulkách.
- Pravidla jen se zdrojem v materiálech; materiály semináře se do repa nekopírují.
- Materiály: složka materiálů semináře SBP (mimo repo); textové převody v `$S/sbp/*.txt` (`$S` = pracovní složka mimo repo).
- Vše ve větvi `pravidla-prace`; na konci squash do jednoho commitu; push/PR jen se souhlasem.

## Review Focus

1. **Pravidlo bez opory v materiálu** — každé nové pravidlo má zdroj, kde to opravdu stojí; úkoly 2–7 mají krok „ověřit tvrzení proti `$S/sbp/*.txt`“.
2. **Tiše vybraná hodnota** u délek a citačních tvarů — každý řádek tabulky rozporů ve specifikaci skončí jako Varianty a v README Rozpory (kontrola `--uplne`, test `test_rozpor_bez_variant`).
3. **Pravidlo bez signálu** — Ověření jen „posouzení“ bez konkrétního vodítka; úkoly mají krok „každé Ověření jmenuje signál“.
4. **Úprava obrázků z APA manuálu** (Times New Roman, název nad obrázkem) prosákne do pravidel — úkol 6 krok `grep -rn "Times New Roman" docs/pravidla` → jen v README v poznámce o starší šabloně / nikde v pravidlech.
5. **Neznámý typ práce** — KAP pravidla musí říct, co dělat, když typ BP nejde určit (úkol 4).

---

### Task 1: Kontrola — nové zdroje, štítek `styl`, pokrytí posudku a materiálů

**Files:** Modify `docs/pravidla/kontrola.py`, `docs/pravidla/test_kontrola.py`, `docs/pravidla/README.md`; add spec + this plan to the commit.

**Interfaces — Produces:**
- `SEMINAR_TEMATA: list[str]` = `["Úvod", "Závěr", "Abstrakt", "Typy BP", "Rešerše", "Citace", "Typografie", "Chyby", "Vyhledávání"]`
- `KRITERIA_POSUDKU: list[str]` = `["Splnění stanovených cílů závěrečné práce", "Význam pro praxi", "Aktuálnost zvoleného tématu", "Použité metody zpracování", "Metody hodnocení výsledků", "Struktura práce", "Práce s odbornou literaturou a citace", "Stylistická kvalita závěrečné práce a formální úroveň textu", "Aktivita a práce studenta při vypracování závěrečné práce"]`
- `MATERIALY_SEMINARE: list[str]` = 22 souborů ze složky SBP mimo `šablona ZP 2023.docx`, `Jak psát práce na VŠPJ.pdf`, `README.md` (přesné názvy včetně přípon).
- `STITKY_CO` += `"styl"`.
- `pokryti.md` v `--uplne`: řádky `| posudek <kritérium> | … |` pro každé kritérium a `| materiál <soubor> | … |` pro každý soubor.

- [ ] **Step 1: Testy** — `test_zdroj_smernice` (`směrnice SP 2/2020 (čl. 5)` OK), `test_zdroj_seminar` (`seminář Úvod` OK), `test_zdroj_seminar_nezname_tema` (`seminář Vaření` → chyba obsahuje „téma“), `test_zdroj_apa` (`APA manuál` OK), `test_stitek_styl` (OK), `test_pokryti_chybi_kriterium` (`uplne`, chybí `posudek Význam pro praxi` → chyba to jméno obsahuje), `test_pokryti_chybi_material` (chybí `materiál desky_bp.pdf`). `uplna_sada` doplnit o řádky pro všechna kritéria a materiály.
- [ ] **Step 2:** `python3 -m pytest -q docs/pravidla` → nové testy FAIL.
- [ ] **Step 3:** Implementovat v `_zkontroluj_zdroj` a `_zkontroluj_uplne`.
- [ ] **Step 4:** `python3 -m pytest -q docs/pravidla` → PASS; `python3 docs/pravidla/kontrola.py` → OK (bez `--uplne`; pokrytí se doplní v úkolu 8).
- [ ] **Step 5: README** — tabulka Zdroje + 3 řádky (tvary ze specifikace), odstavec „Materiály semináře nejsou v repu; pravidla, jejichž jediným zdrojem je `seminář …`, jsou doporučení Katedry technických studií — kontrola je hlásí jako upozornění“; seznam témat; štítek `styl` do tabulky Štítky; APA jako rovnocenná varianta citací.
- [ ] **Step 6: Commit** — `docs(pravidla): zdroje pro obsahová pravidla`.

### Task 2: Abstrakt a klíčová slova (`stranky/abstrakt.md`)

**Consumes:** zdroje z úkolu 1. **Produces:** `ABS-O*`.

- [ ] **Step 1:** `Účel:` (vyhledávání; rozhodnutí, zda práci číst; samostatný text). Pravidla: struktura problém–metody–výsledky–závěry; lineární nebo globální typ; samostatně srozumitelný (bez nevysvětlených zkratek, rovnic, obrázků, tabulek, citací); neslibuje nic, co v práci není; **délka** s Variantami ≤ 150 slov (šablona pokyn na straně Abstrakt) × 8–10 řádků (seminář Abstrakt) × ≤ 250 slov (seminář Abstrakt — norma); klíčová slova 3–7 (existující ABS-O02) + odborné termíny, podstatná/přídavná jména a slovní spojení, ne věty, ne stop-slova (seminář Abstrakt; seminář Vyhledávání); anglický překlad obsahově shodný (existující ABS-O03). Existující ABS-O01 (≤ 150 slov) zúžit/převést na délku s variantami.
- [ ] **Step 2:** Ověřit každé tvrzení v `$S/sbp/abstrakt.txt`, `sbp7_abstrakt.txt`, `tipy_na_vyhledávání.txt`; každé Ověření jmenuje signál.
- [ ] **Step 3:** `python3 docs/pravidla/kontrola.py` → OK. **Step 4: Commit.**

### Task 3: Úvod (`stranky/uvod.md`)

**Produces:** `UVO-O*`, `UVO-F02`.

- [ ] **Step 1:** `Účel:` (první dojem, výchozí bod, ne parafráze abstraktu). Pravidla: vychází ze zadání; definuje problém / předmět a stav poznání; motivace a kritéria volby, vztah k programu; hlavní cíl a dílčí cíle jasně (signál „Cílem práce je…“); metody obecně; přínos; zákaz výsledků; zákaz parafráze abstraktu; osobnější styl jen u motivace (viz DOK styl); **délka** Varianty: přiměřená (šablona) × ≈ 3 strany (seminář Úvod; seminář Rešerše). Formální `UVO-F02` „bez podkapitol a podnadpisů“ (seminář Úvod). Existující UVO-O01 zúžit na „cíl práce“ nebo „motivace“ dle spec.
- [ ] **Step 2:** Ověřit proti `uvod.txt`, `SBP_CVIČ2.txt`, `sbp_rešerše.txt`; signály.
- [ ] **Step 3:** kontrola OK. **Step 4: Commit.**

### Task 4: Kapitoly a typ práce (`stranky/kapitola.md`, `stranky/prilohy.md`)

**Produces:** `KAP-O*`, `PRI-O*`.

- [ ] **Step 1:** `Účel:` jádra práce. Pravidla: teoretická část = stav poznání a vymezení pojmů (seminář Rešerše); rešerše typicky v 1.1 a vlastní práce na ni reaguje; **určení typu BP** (implementační / návrhová / srovnávací / kombinovaná) ze zadání nebo cíle v úvodu, u kombinované musí být stěžejní část zřejmá; **fallback**: typ nejde určit → kontrolují se jen společné prvky a skill upozorní; jedno pravidlo na typ s doporučenou osnovou ze `seminář Typy BP` (implementační: zdůvodnění volby prostředí, popis implementace (nestandardní části), návod ≤ 2 strany, instalace/spuštění, testy, srovnání; návrhová: analýza a varianty, zdůvodněný návrh, ověření (verifikace/simulace), srovnání; srovnávací: popis systémů, kritéria, metodika, výsledky, zobecnění); společné: popis struktury práce ve vztahu k cílům. `PRI-O*`: u implementační práce dokumentace, zdrojový kód, instalační/uživatelská příručka jako příloha.
- [ ] **Step 2:** Ověřit proti `sbp_cvič1.txt`, `sbp_rešerše.txt`; signály.
- [ ] **Step 3:** kontrola OK. **Step 4: Commit.**

### Task 5: Závěr (`stranky/zaver.md`)

**Produces:** `ZAV-O*`.

- [ ] **Step 1:** `Účel:` kritické zhodnocení. Pravidla: každý cíl z úvodu se hodnotí (úplně/částečně/ne, s důvodem) — vazba na `UVO-O` cíl; přehled výsledků, ne shrnutí celé práce; přínos a co je nad rámec zadání; problémy a jejich řešení, omezení platnosti; pokračování a doporučení pro praxi; odpovědi na hypotézy / výzkumnou otázku; minulý čas; implementační web: kde aplikaci spustit (seminář Typy BP); **délka** Varianty ≤ 2 strany × 2–3 strany (obojí seminář Závěr). Existující ZAV-O01 rozdělit.
- [ ] **Step 2:** Ověřit proti `co_ma_byt_v_zaveru.txt`, `psaní závěru.txt`; signály.
- [ ] **Step 3:** kontrola OK. **Step 4: Commit.**

### Task 6: Citace a APA (`prvky/odkaz-v-textu.md`, `prvky/polozka-literatury.md`)

**Produces:** `CIT-O*`, upravené `CIT-F*`, `BIB-F*`.

- [ ] **Step 1:** Obsahová: přímá citace jen s důvodem; doslovná, vynechání `[…]`, chyby `[sic]`; parafráze skutečně přeformulovaná (mozaika = plagiát); vše převzaté se zdrojem (myšlenky, fakta, obrázky, statistiky); autocitace citovat; necitovat nepoužité zdroje (seminář Citace; směrnice SP 2/2020 čl. 5 — plagiátorství). Formální Varianty doplnit: CIT-F01 harvard (příručka) × APA (`APA manuál`) × „str.“ (seminář Citace); CIT-F03 „a kol.“ od 4 × „et al.“ od 3 (APA); spojka „a“ × „&“; odkaz na více zdrojů středníkem (APA); sekundární citace (seminář Citace); CIT-F05 přímá citace: uvozovky nebo kurzíva (příručka) × uvozovky bez kurzívy, nad 40 slov blok 10 pt (APA); BIB-F03 tvar ČSN ISO 690 × APA „Příjmení, I. (Rok). Název. Nakladatel. DOI“; BIB-F04 řazení + APA chronologicky u stejného autora; BIB-O01 všichni autoři do 20 (APA).
- [ ] **Step 2:** Ověřit proti `citace 2.txt`, `citace.txt`, `Citační manuál APA.txt`; `grep -rn "Times New Roman" docs/pravidla/prvky docs/pravidla/stranky docs/pravidla/dokument.md` → nic.
- [ ] **Step 3:** kontrola OK. **Step 4: Commit.**

### Task 7: Odborný styl a celek (`dokument.md`)

**Produces:** `DOK-O*`; zdroj navíc u `DOK-F10`.

- [ ] **Step 1:** Odborný styl: bez první osoby, není-li důvod (seminář Úvod); bez hovorových a citově zabarvených výrazů; bez zbytečného opakování, nejednoznačností (seminář Úvod; seminář Závěr); správné odborné termíny jednotně (seminář Chyby; seminář Abstrakt); věta nezačíná číslicí; čísla a slova se nekombinují (seminář Typografie, doplnit k DOK-O02); název odpovídá obsahu a obsah zadání (seminář Chyby); bez citlivých osobních údajů (směrnice SP 2/2020 čl. 3); DOK-F10 varianta b) doplnit zdroj `seminář Typografie`. Štítek `styl`. Navíc formální `DOK-F20 Rozsah práce` (zdroj `rozhodnutí repa`; potvrzeno uživatelem): vlastní text = stránky od Úvodu po Závěr včetně; skill vždy uvede počet stran, slov a normostran (1 800 znaků); když zadání (s. 2) rozsah uvádí, porovná, jinak napíše, že požadovaný rozsah nezná — nehodnotí. Do README „Nepopsané prvky“ přidat „celkový rozsah práce (požadavky nejsou v materiálech; viz DOK-F20)“.
- [ ] **Step 2:** Ověřit proti `SBP_CVIČ2.txt`, `typografie.txt`, `typografie_prezentace.txt`, `chyby_v__pracich.txt`, `Směrnice BP 2020.txt`.
- [ ] **Step 3:** kontrola OK. **Step 4: Commit.**

### Task 8: Rozpory a pokrytí

**Files:** Modify `docs/pravidla/README.md`, `docs/pravidla/pokryti.md`.

- [ ] **Step 1:** README Rozpory — řádky ze specifikace (délka abstraktu, závěru, úvodu; strana v citaci; spojka autorů; „a kol.“ / „et al.“) s ID pravidel.
- [ ] **Step 2:** `pokryti.md` — sekce Kritéria posudku (9 řádků, nekontrolovatelná `vynecháno: …`, např. Aktivita studenta, Význam pro praxi jen částečně) a Materiály semináře (22 řádků; nepoužité `vynecháno: …` podle specifikace).
- [ ] **Step 3:** `python3 docs/pravidla/kontrola.py --uplne` → OK; `python3 -m pytest -q docs/pravidla` → PASS.
- [ ] **Step 4:** Squash větve do jednoho commitu (`git reset --soft b0c12c2` + commit se souhrnnou zprávou), znovu spustit obě kontroly.
