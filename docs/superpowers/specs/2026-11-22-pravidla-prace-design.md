# Popis pravidel závěrečné práce VŠPJ — návrh

Datum: 2026-11-22
Stav: schváleno (2026-11-22)

## Záměr

Chceme mít na jednom místě sepsané, jak má vypadat závěrečná práce na VŠPJ:
každý typ stránky (titulní strana, úvod, závěr…), každý prvek (obrázek, tabulka,
nadpis…) a pravidla platná pro celý dokument (okraje, písmo, číslování…).

Popisy jsou **podklad pro pozdější skill**, který zkontroluje odevzdávanou práci
(její PDF) a upozorní na pravděpodobné chyby. Skill se navrhne zvlášť, až budou
popisy hotové. Popisy musí být zároveň čitelné pro člověka (na GitHubu), aby se
daly ověřit proti zdrojům a doplňovat.

## Cíle

- Pro každý typ (seznam níže) sepsat pravidla ve dvou kategoriích:
  - **Formální** — písmo, řez, velikost, zarovnání, mezery, odsazení, umístění,
    číslování, pořadí.
  - **Obsahová** — co má daná část obsahovat (např. úvod: cíl práce, motivace).
- U každého pravidla uvést zdroj a ověřitelnou hodnotu.
- Tam, kde si zdroje odporují, uvést **všechny varianty** se zdroji.
- U každého pravidla uvést, zda jde ověřit z PDF, nebo jen ze zdroje (DOCX/.tex).

## Ne-cíle

- Samotný kontrolní skill, měřicí skripty a prahové hodnoty — další fáze.
- Rozhodování rozporů mezi zdroji. Popisy rozpory jen zaznamenají.
- Seminární práce (příručka kap. 11.2, číslování „1/5“). Šablona je jen pro
  závěrečnou práci. *(moje rozhodnutí)*
- Úpravy LaTeX šablony. LaTeX šablona a její PDF **nejsou zdroj pravidel** —
  jsou to výstup, který podle pravidel upravujeme a který skill později kontroluje.

## Anti-cíle (co by bylo selháním, i kdyby to „fungovalo“)

- Pravidlo bez zdroje nebo s hodnotou, kterou nejde dohledat ve zdroji
  ani změřit ve Word PDF.
- Tiché vybrání jedné varianty při rozporu.
- Pravidla vázaná na konkrétní text (jméno, název práce). Kontroluje se formát,
  ne znění — výjimkou jsou pevné texty (např. „Bakalářská práce“, nadpis „Abstrakt“).
- Pravidla formulovaná tak, že je nejde ověřit z PDF ani ze zdroje
  (např. „text má být čitelný“).

## Zdroje

Pořadí odpovídá důležitosti, ale **nerozhoduje rozpory** — viz Varianty.

1. **Příručka** „Jak psát práce na VŠPJ: Typografická pravidla pro studenty VŠPJ“
   (Borůvková a kol., 2021). Text DOCX od uživatele
   (`~/Downloads/jakpsatpracenavspj-…-finalniverzebezkomentarudocx-….docx`) je
   shodný s PDF z října 2021 i s `Dokumenty/Jak psát práce na VŠPJ.pdf` v repu
   (liší se jen tiráží). Odkazuje se kapitolou, např. „příručka 6.2“.
2. **Šablona DOCX** `Dokumenty/Sablona.docx` (verze 2023). Používá se:
   - definice stylů (`word/styles.xml`): Normální, Nadpis 1–3, Název, Titulek,
     Zdroj, Tabulka, Seznam literatury, Obsah 1–2, Text poznámky pod čarou;
   - oddíly (`sectPr`): okraje, záhlaví/zápatí, pole PAGE, svislé zarovnání;
   - přímé formátování odstavců (titulní strana, prohlášení);
   - **pokyny v šabloně** (modré texty, např. „Abstrakt v českém jazyce,
     max. 150 slov“) — hlavní zdroj obsahové kategorie.
   Odkazuje se stylem nebo místem, např. „šablona styl Titulek“,
   „šablona oddíl 3 (vAlign=bottom)“.
3. **Word PDF** `Dokumenty/Sablona.pdf` — export šablony z Word Online.
   Slouží jako vizuální reference (proti němu se později dělá vizuální
   crosscheck LaTeX PDF) a zdroj **změřených** hodnot tam, kde DOCX
   hodnotu přímo neříká (polohy na titulní straně, skutečná výška řádku,
   poloha čísla stránky). Odkazuje se „Word PDF s. N“ a hodnota je označena
   jako změřená.

Aktuální verze příručky i šablony jsou na https://kts.vspj.cz/cs/statni-zaverecne-zkousky/zaverecne-prace a na https://is.vspj.cz/dokumentace-student/; README v `docs/pravidla/` je uvede, aby šlo zdroje při nové verzi obnovit.

LibreOffice export se jako zdroj nepoužívá (vykresluje šablonu jinak,
viz `Dokumenty/README.MD`).

## Typy (soubory)

Umístění: `docs/pravidla/` v repu šablony. *(moje rozhodnutí)*
Každý typ = jeden soubor, prefix = začátek ID pravidel.

**Celý dokument** — `dokument.md`, prefix `DOK`
okraje a formát papíru, základní písmo a odstavec (Normální), zarovnání,
řádkování, mezery mezi odstavci, záhlaví, číslování stránek (které strany se
počítají / zobrazují, poloha), dělení slov, pevné mezery a jednopísmenné
předložky, sirotci a vdovy, zvýrazňování, uvozovky a pomlčky, čísla a jednotky,
počet úrovní nadpisů, každá kapitola na nové stránce, pořadí povinných částí.

**Stránky** — `stranky/<typ>.md`
| Soubor | Prefix |
|---|---|
| titulni-strana | TIT |
| zadani | ZAD |
| abstrakt (vč. Klíčová slova, Abstract, Keywords) | ABS |
| prohlaseni | PRO |
| podekovani | POD |
| obsah | OBS |
| seznam-obrazku | SOB |
| seznam-tabulek | STA |
| seznam-zkratek | SZK |
| uvod | UVO |
| kapitola (běžná kapitola textu) | KAP |
| zaver | ZAV |
| seznam-literatury | LIT |
| prilohy | PRI |

**Prvky** — `prvky/<typ>.md`
| Soubor | Prefix |
|---|---|
| nadpis-1, nadpis-2, nadpis-3 | NA1, NA2, NA3 |
| obrazek (vč. grafů) | OBR |
| tabulka | TAB |
| rovnice | ROV |
| vycet-seznam | VYC |
| odkaz-v-textu (citace v textu) | CIT |
| poznamka-pod-carou | PPC |
| polozka-literatury | BIB |

Pravidlo platné pro víc typů se zapíše jednou (u nejobecnějšího typu)
a ostatní na něj odkazují ID.

## Formát souboru

```markdown
# Obrázek

Krátký popis, kde se typ v práci vyskytuje.

## Formální

### OBR-03 Titulek pod obrázkem
- Pravidlo: Titulek je pod obrázkem, Calibri 10 b., tučně, na střed, mezera za 0 b.
- Zdroj: šablona styl Titulek; příručka 3, 6.2
- Varianty: —
- Ověření: PDF — řádek pod obrázkem, výška písma ≈ 10 b., tučný, na střed
- Poznámka: (volitelné)

## Obsahová

### OBR-20 Titulek popisuje obsah obrázku
- Pravidlo: …
- Zdroj: …
- Ověření: PDF (posouzení textu)
```

Pole:
- **ID** — `PREFIX-NN`, čísla se nepřečíslovávají (smazané ID se nepoužije znovu).
  Formální 01–19, obsahová 20+ (aby šlo přidávat bez přečíslování).
- **Pravidlo** — jedna věta, hodnoty v bodech (pt) s jednotkou. Převody:
  twips / 20 = pt, `sz` / 2 = pt, `line=276` = 1,15 řádku.
- **Zdroj** — jeden nebo víc odkazů ve tvaru ze sekce Zdroje.
- **Varianty** — viz níže; „—“ když rozpor není.
- **Ověření** — `PDF`, `zdroj` nebo `PDF + zdroj`, a krátce co se v PDF hledá.
  Konkrétní tolerance zde jen orientačně, definitivní budou ve skillu.
- **Poznámka** — vysvětlení, proč pravidlo vypadá, jak vypadá (volitelné).

`docs/pravidla/README.md` obsahuje: účel, seznam souborů, popis formátu,
zásady pro varianty, převody jednotek a seznam všech rozporů (odkazy na ID).

## Varianty (rozpory mezi zdroji)

Když si zdroje odporují (příručka × šablona DOCX × Word PDF), pravidlo uvede
všechny varianty, každou se zdrojem:

```
- Varianty:
  - a) na střed — příručka 3 (Tab. 1)
  - b) vlevo — šablona styl Nadpis 1 (jc=left), Word PDF s. 11
```

Při kontrole bude **vyhovovat kterákoli varianta**; skill jen poznamená,
že se zdroje rozcházejí. Za chybu se považuje až stav, který neodpovídá žádné.

Rozpory známé už teď (musí se v popisech objevit):
| Téma | Příručka | Šablona DOCX / Word PDF |
|---|---|---|
| Zarovnání Nadpisu 1 | na střed (Tab. 1) | vlevo (styl i PDF) |
| Text v tabulce | 11/10 b., na střed | styl Tabulka 10 b., vlevo |
| Označení příloh | „Příloha 1, 2…“ | „Příloha A.1, B.2…“ |
| Číslování stránek příloh | nečíslují se | „nemusí se číslovat v návaznosti“ |
| Tučné v textu | nepoužívá se | „omezeně lze“ |
| Zdroj pod obrázkem | „zdroj:“ (příklad) | „Zdroj:“ |
| První číslovaná strana | Obsah (zpravidla 6) | pole PAGE až od Úvodu (oddíl 6) |
| Dělení slov | nutné u zarovnání do bloku | šablona automatické dělení nemá |
| Poděkování | — | oddíl vAlign=bottom → ve Word PDF dole na stránce |
| Název stylu literatury | „Bibliografie“ | „Seznam literatury“ |

## Obsahová kategorie

Uživatel ji dopracuje na závěr z dalších materiálů. Teď se do ní zapíše jen to,
co je výslovně ve zdrojích, např.:
- abstrakt max. 150 slov, 3–7 klíčových slov oddělených středníkem, anglický překlad
  obojího (šablona);
- úvod: cíl práce, motivace k výběru tématu, aktuálnost (šablona);
- závěr: odpověď na výzkumnou otázku, zhodnocení hypotéz, přínos autora,
  využitelnost výsledků, další směry (šablona);
- přílohy: co do nich patří, na každou se v textu odkazuje (šablona, příručka 13);
- seznamy obrázků/tabulek až od 5 položek (šablona, příručka 6.3);
- obsah jen první dvě úrovně, bez sebe sama a úvodních stran (šablona, příručka 5.3);
- každá položka literatury je citovaná v textu, řazení abecedně (příručka 7.1);
- mezi nadpisy různých úrovní a mezi nadpisem a obrázkem/tabulkou/výčtem aspoň
  jeden odstavec (příručka 3, 5.2, 6).

Sekce `## Obsahová` je v každém souboru, i když prázdná (s poznámkou
„k doplnění“).

## Postup

1. `README.md` (formát, zdroje, tabulka rozporů).
2. `dokument.md` — ostatní soubory na něj odkazují.
3. Prvky (nadpisy, obrázek, tabulka…).
4. Stránky.
5. Kontrolní průchod: každá kapitola příručky, každý styl a oddíl šablony
   a každý pokyn v šabloně je pokrytý aspoň jedním pravidlem (nebo výslovně
   vynechán s důvodem — např. seminární práce).

Hodnoty z DOCX se čtou přímo z XML. Hodnoty z Word PDF se měří z vykreslené
stránky (řádky podle inkoustu, poloha čísla stránky); lze použít pomocné
skripty z dřívější práce na šabloně. Skripty se do repa v této fázi
neukládají — patří ke skillu. *(moje rozhodnutí)*

## Další rozhodnutí *(moje rozhodnutí)*

- **Písmo:** pravidla uvádějí Calibri / Calibri Light (šablona, příručka 3)
  a jako přijatelnou náhradu metricky shodné Carlito (Calibri není volně
  šiřitelné, v CI ho mít nelze). Náhrada se zapíše jako varianta s poznámkou.
  *(potvrzeno uživatelem)*
- **Rozsah:** jen bakalářská a diplomová práce v češtině (šablona je společná,
  liší se jen text „Bakalářská/Diplomová práce“). *(potvrzeno uživatelem)*

## Co je ponecháno na tom, kdo popisy píše

- Přesné formulace pravidel a jejich rozdělení do ID.
- Které obecné pravidlo patří do `dokument.md` a které k typu.
- Orientační tolerance v poli Ověření.
- Jak podrobně popsat titulní stranu (doporučeno: polohy hlavních řádků
  změřené z Word PDF, ne počty prázdných odstavců).

## Další fáze (mimo tento návrh)

Skill nad popisy: vstupem PDF (výstup LaTeX šablony nebo vypracovaná práce),
volitelně zdroj (.tex/DOCX); podle ID pravidel změří a posoudí, vizuálně
porovná s Word PDF a vypíše upozornění s odkazy na ID. Vše, co řeší samotné
porovnávání a kontrolu (skripty, tolerance), patří ke skillu.
Návrh skillu proběhne samostatně.

## Doplněk (2026-11-22, po první verzi)

Rozhodnutí uživatele po zhodnocení první verze:

- **Rozpoznání:** každý soubor stránky a prvku má sekci `## Rozpoznání`.
  Pořadí částí je pevné, úvodní strany mají pevnou fyzickou stranu, další
  části se poznají podle nadpisu 1. úrovně.
- **Nepopsané prvky** (zdrojový kód, tabulka přes více stránek, stránka na
  šířku…) se doplní, až na ně dojde. Do té doby je kontrola jen zmíní
  a upozorní, že si jejich formátem není jistá (README, „Nepopsané prvky“).
- **Chyby LaTeXu** jsou popsané v `latex-chyby.md` (prefix LTX) s příznakem
  v PDF / logu a odkazem na porušené pravidlo.
- **ID:** `PREFIX-F01` formální, `PREFIX-O01` obsahová (nahrazuje rozsahy
  01–19 / 20–99).
- **Štítky:** povinné pole `Štítky` ze slovníku (co + jak se ověřuje) místo
  dělení velkých pravidel.
- Měření z jediného vzorku (Word PDF šablony) zůstávají — jiný zdroj není.
