# Obsahová pravidla závěrečné práce — návrh

Datum: 2026-11-22
Stav: schváleno (2026-11-22)
Navazuje na: `2026-11-22-pravidla-prace-design.md` (formální pravidla, formát, štítky)

## Záměr

Doplnit do `docs/pravidla/` sekce `## Obsahová` tak, aby kontrolní skill uměl
posoudit, zda je každá část práce **napsaná jako ta část**: je úvod opravdu
úvod (problém, motivace, cíl, metody — bez výsledků)? Je závěr opravdu závěr
(hodnocení splnění cílů, ne shrnutí)? Plní abstrakt roli abstraktu? Hlášení
má autorovi říct, co konkrétně chybí nebo je navíc.

## Cíle

- Pro každou část s obsahovou rolí sepsat pravidla „úkon po úkonu“: jedna role
  nebo jeden zákaz = jedno pravidlo `XXX-Onn`.
- Na začátek každé sekce `## Obsahová` krátký odstavec **Účel** (k čemu část
  slouží), aby skill měl kontext pro posouzení.
- U každého pravidla v poli Ověření uvést **signály v textu**, podle kterých se
  rozhoduje (např. „formulace typu ‚Cílem práce je…‘“, „čas sloves minulý“).
- Zapsat vazby mezi částmi (úvod ↔ závěr, abstrakt ↔ celá práce, název ↔ obsah).
- Přidat APA jako rovnocennou variantu citačních pravidel.
- Ověřit pokrytí kritérií posudku vedoucího a oponenta (Směrnice, přílohy 1–2).

## Ne-cíle

- Postup práce: vyhledávání literatury, postup rešerše, harmonogram, způsob
  odevzdání (soubory v IS, podpisy), desky a hřbet.
- Hodnocení odborné správnosti (funkčnost programu, správnost návrhu databáze,
  volba metod v oboru) — to je práce vedoucího a oponenta.
- Hodnocení „aktivity studenta“ a dalších kritérií posudku, která z textu nejdou
  poznat.
- Matematická sazba a další formální doplňky z materiálů semináře.
  *(potvrzeno uživatelem)*
- Ukládání materiálů semináře do repa (repo je veřejné, materiály patří
  vyučujícím); pravidla na ně jen odkazují. *(potvrzeno uživatelem)*

## Anti-cíle

- Pravidlo, které žádný materiál neříká (vymyšlené „dobré praxe“).
- Pravidlo závislé na konkrétním tématu práce.
- Pravidlo bez signálu v Ověření — skill by neměl podle čeho rozhodnout.
- Tichý výběr jedné hodnoty tam, kde si materiály odporují.

## Zdroje (nové)

Doplňují zdroje z první části (příručka, šablona, Word PDF).

| Tvar ve Zdroji | Dokument | Váha |
|---|---|---|
| `směrnice SP 2/2020 (čl. N)` / `směrnice SP 2/2020 (příloha 1)` | Směrnice pro vedení, vypracování a zveřejňování závěrečných prací na VŠPJ, SP č. 2/2020 | závazná |
| `seminář <téma>` | materiály Semináře k bakalářské práci (SBP), Katedra technických studií; témata viz níže | doporučení katedry |
| `APA manuál` | Manuál pro citační normu APA, 7. vydání (Ústav pedagogických věd) — jen citace | rovnocenná varianta citací |

Témata `seminář …` a soubory, ze kterých se čerpá (v složka materiálů semináře SBP (mimo repo)):

| Téma ve Zdroji | Soubor(y) |
|---|---|
| `seminář Úvod` | `uvod.doc`, `SBP_CVIČ2.pptx` |
| `seminář Závěr` | `co_ma_byt_v_zaveru.doc`, `psaní závěru.pptx` |
| `seminář Abstrakt` | `abstrakt.doc`, `sbp7_abstrakt.pptx` |
| `seminář Typy BP` | `sbp_cvič1.ppt` |
| `seminář Rešerše` | `sbp_rešerše.pptx` (jen umístění a role rešerše v práci) |
| `seminář Citace` | `citace 2.pptx`, `citace.ppt` (starší norma — jen obecné zásady), `harvard odkazy.pdf` |
| `seminář Typografie` | `typografie.pdf`, `typografie_prezentace.pptx` |
| `seminář Chyby` | `chyby_v__pracich.ppt` |
| `seminář Vyhledávání` | `tipy_na_vyhledávání.pdf` (jen klíčová slova) |

Nepoužívá se: `harmonogram_ZP_leden_27.docx`, `rešerše.docx` (články o postupu),
`desky_bp.pdf`, `Matematicka_sazba_c3.pdf`, `prohlaseni.doc` (starší znění),
údaj o „šabloně VŠPJ s Times New Roman 12“ v `typografie_prezentace.pptx`
(starší šablona). Důvod se zapíše do `pokryti.md`.

`kontrola.py` se rozšíří o tyto tvary zdroje (seznam témat semináře pevný).
README dostane řádky do tabulky Zdroje a poznámku, že materiály semináře nejsou
v repu.

**APA:** citace podle APA manuálu jsou v práci přípustné stejně jako harvardský
styl podle příručky — rovnocenná varianta, bez výhrady. *(potvrzeno
uživatelem)* Z manuálu se berou jen citace v textu a seznam literatury;
jeho úprava obrázků, grafů a tabulek (Times New Roman 12, název nad obrázkem)
se **nepřebírá** — odporuje šabloně VŠPJ.

## Platnost pravidel ze semináře

Materiály semináře jsou katedrové (KTS). Pravidla, jejichž jediným zdrojem je
`seminář …`, platí jako doporučení katedry; README to uvede a skill je hlásí jako
upozornění, ne jako chybu. *(potvrzeno uživatelem)*

## Pravidla k sepsání (rozsah)

Čísla jsou orientační, zachovávají se už existující obsahová ID
(ID se nepřečíslovávají, nová dostanou další volné číslo). Existující pravidlo,
které nový výčet rozdělí na víc rolí (např. UVO-O01 „cíl, motivace,
aktuálnost“), se zúží na jednu roli a zbytek dostane nová ID; pravidlo
nahrazené úplně se smaže a jeho ID se znovu nepoužije. *(potvrzeno uživatelem)*

**Abstrakt (ABS-O)** — účel: samostatné shrnutí pro vyhledávání a rozhodnutí,
zda práci číst. Role: problém – metody – výsledky – závěry; srozumitelný bez
zbytku práce; bez zkratek, rovnic, obrázků, citací; neslibuje nic, co v práci
není; lineární nebo globální typ. Délka — varianty: ≤ 150 slov (šablona),
8–10 řádků (seminář Abstrakt), do 250 slov (norma, zmíněno v semináři).
Klíčová slova: 3–7, odborné termíny (podstatná a přídavná jména, slovní
spojení), ne věty ani stop-slova; anglický překlad obsahově shodný.

**Úvod (UVO-O)** — účel: první dojem, výchozí bod pro čtenáře. Role: vychází ze
zadání; definuje problém / předmět; motivace a kritéria volby tématu, vztah
k oboru; jasný hlavní cíl a dílčí cíle; obecně metody (případně proč ne jiné);
přínos práce. Zákazy: výsledky; parafráze abstraktu; podkapitoly a podnadpisy
(obnoví vyřazené pravidlo bez podkapitol, teď se zdrojem `seminář Úvod`).
Délka: přiměřená, typicky ≈ 3 strany (úvod 2 + motivace ½ + cíl ½).
Osobnější styl připuštěn jen pro motivaci.

**Kapitola (KAP-O)** — účel: jádro práce. Teoretická část: současný stav
poznání, vymezení pojmů; rešerše typicky v podkapitole 1.1 a vlastní práce na
ni reaguje. **Typ práce** (implementační / návrhová / srovnávací /
kombinovaná) a doporučená osnova každého typu (`seminář Typy BP`), např.
implementační: zdůvodnění volby prostředí, popis implementace, návod
nejvýše 2 strany, výsledky testování, srovnání s existujícími řešeními.
Rozpoznání typu: ze zadání nebo z cíle v úvodu; když nejde určit, skill
kontroluje jen společné prvky a upozorní, že typ nezná.

**Závěr (ZAV-O)** — účel: kritické zhodnocení, odpověď na cíle. Role:
rekapitulace cílů z úvodu a hodnocení míry splnění (úplně / částečně / ne,
s důvodem); přehled výsledků (ne shrnutí celé práce); přínos autora, co je
nad rámec zadání; problémy a jejich řešení, omezení platnosti; možnosti
pokračování a doporučení pro praxi; odpovědi na hypotézy / výzkumné otázky;
u webové aplikace kde ji lze spustit (implementační práce). Minulý čas.
Délka — varianty: nejvýš 2 strany (seminář Závěr, slajdy) × 2–3 strany
(seminář Závěr, dokument). Vazba: každý cíl z úvodu se v závěru hodnotí.

**Citace v textu (CIT-O, CIT-F)** — přímá citace jen s důvodem; doslovná
(beze změn, vynechání `[…]`, chyby `[sic]`); parafráze skutečně přeformulovaná
(přeházená slova = mozaikový plagiát); vše převzaté (myšlenky, fakta, obrázky,
statistiky) se zdrojem; autocitace také; necitovat nepoužité zdroje. Formální
varianty (do existujících CIT-F a BIB-F): „s.“ (příručka) × „str.“ (seminář
Citace); „a“ × „&“; sekundární citace „(Pol 2006, In Molnár 2009)“;
**APA** — „(Barrow & Keeney, 2001)“, „et al.“ od tří autorů, odkaz na více
zdrojů středníkem, přímá citace nad 40 slov jako blok 10 pt bez uvozovek,
seznam: „Příjmení, I. (Rok). Název. Nakladatel.“, DOI jako `https://doi.org/…`,
všichni autoři do 20.

**Celý dokument (DOK-O)** — odborný styl: bez první osoby, pokud k ní není
důvod; bez hovorových a citově zabarvených výrazů; bez zbytečného opakování;
odborné termíny správně a jednotně. Věta nezačíná číslicí; čísla a slova se
nekombinují („5 tisíc“). Název práce odpovídá obsahu a obsah odpovídá zadání.
Práce neobsahuje citlivé osobní údaje (směrnice). Nevysvětlené zkratky
(navazuje na DOK-O01).

**Přílohy (PRI-O)** — u implementační práce kompletní dokumentace, zdrojový
kód, instalační / uživatelská příručka jako (elektronická) příloha
(`seminář Typy BP`).

**Ostatní** — prohlášení, zadání, poděkování: obsahová pravidla už jsou;
bez změny.

## Rozpory a varianty

Zapíší se jako varianty a přidají do tabulky Rozpory v README:

| Téma | Varianty |
|---|---|
| Délka abstraktu | ≤ 150 slov (šablona) × 8–10 řádků (seminář) × ≤ 250 slov (norma podle semináře) |
| Délka závěru | ≤ 2 strany × 2–3 strany (oba seminář Závěr) |
| Délka úvodu | „přiměřená“ (šablona) × ≈ 3 strany (seminář Úvod, Rešerše) |
| Strana v citaci | „s.“ (příručka) × „str.“ (seminář Citace) × „s.“ s pomlčkou rozsahu (APA) |
| Spojka autorů | „a“ (příručka) × „&“ (seminář Citace, APA) |
| Počet autorů pro „a kol.“ / „et al.“ | od 4 (příručka) × od 3 (APA) |
| Dělení slov | doplnit zdroj `seminář Typografie` k variantě „nedělit“ v DOK-F10 |

## Kontrola pokrytí

`pokryti.md` dostane sekce:
- **Kritéria posudku** — 9 kritérií z přílohy 1 Směrnice; každé → ID pravidel
  nebo `vynecháno: důvod` (např. „Aktivita studenta“ — nejde poznat z textu).
- **Materiály semináře** — každý soubor → použitý (s ID) nebo
  `vynecháno: důvod`.

`kontrola.py --uplne` vynutí řádek pro každé kritérium (pevný seznam
`KRITERIA_POSUDKU`) a pro každý soubor semináře (pevný seznam).

## Formát

Beze změny proti první části (ID `XXX-Onn`, pole, štítky). Obsahová pravidla
mají ve Štítcích vždy `obsah-textu` a aspoň `posouzení` nebo `text`. Pole
Ověření začíná `PDF — ` a pokračuje signály. Odstavec **Účel** je volný text
mezi `## Obsahová` a prvním pravidlem (kontrola ho ignoruje).

Do slovníku štítků přibude `styl` (odborný styl textu). *(potvrzeno uživatelem)*

## Co je ponecháno na tom, kdo pravidla píše

- Přesné rozdělení rolí do pravidel a jejich pořadí.
- Formulace signálů v Ověření.
- Zda doporučenou osnovu typu BP zapsat jako jedno pravidlo na typ, nebo
  pravidlo na prvek osnovy (doporučeno: jedno na typ + společné prvky zvlášť).

## Doručení

Ve stejné větvi `pravidla-prace`; na konci se vše sloučí do jednoho commitu
(přání uživatele).
