# Pravidla závěrečné práce VŠPJ

Popis toho, jak má vypadat bakalářská a diplomová práce na VŠPJ (v češtině):
každý typ stránky, každý prvek a pravidla pro celý dokument. Popisy jsou
podkladem pro kontrolní skill, který porovná PDF práce s pravidly a upozorní
na pravděpodobné chyby. Zároveň mají být čitelné pro člověka, aby se daly
ověřit proti zdrojům a doplňovat.

LaTeX šablona v tomto repu **není** zdrojem pravidel — je to výstup, který se
podle pravidel upravuje a kontroluje.

## Zdroje

| Zkratka v pravidlech | Dokument | Co se z něj bere |
|---|---|---|
| `příručka X.Y` | [Jak psát práce na VŠPJ: Typografická pravidla pro studenty VŠPJ](../../Dokumenty/Jak%20psát%20práce%20na%20VŠPJ.pdf) (Borůvková a kol., 2021), kapitola X.Y | typografická pravidla |
| `šablona …` | [Sablona.docx](../../Dokumenty/Sablona.docx) (verze 2023) — `šablona styl Titulek`, `šablona oddíl 3`, `šablona pokyn (…)`, `šablona titulní strana` | styly, oddíly (okraje, záhlaví, zápatí, číslování), přímé formátování, pokyny v šabloně |
| `Word PDF s. N` | [Sablona.pdf](../../Dokumenty/Sablona.pdf) — export šablony z Word Online | vizuální reference; `(změřeno)` = hodnota změřená z vykreslené stránky |
| `směrnice SP 2/2020` | Směrnice pro vedení, vypracování a zveřejňování závěrečných prací na VŠPJ, SP č. 2/2020 (IS VŠPJ); může následovat `(čl. N)` / `(příloha 1)` | závazné náležitosti, kritéria posudku |
| `seminář <téma>` | materiály Semináře k bakalářské práci (SBP), Katedra technických studií — témata níže | obsah částí práce, odborný styl, citace |
| `APA manuál` | Manuál pro citační normu APA, 7. vydání (s drobnými úpravami pro češtinu), Ústav pedagogických věd (není dokument VŠPJ) | **jen citace** v textu a seznam literatury — rovnocenná varianta k harvardskému stylu rozhodnutím uživatele |

`N` u Word PDF je **fyzická strana PDF** (1–17), ne tištěné číslo stránky:
1 titulní, 2 zadání, 3 abstrakt, 4 prohlášení, 5 poděkování, 6 obsah,
7 seznam obrázků, 8 seznam tabulek, 9 seznam zkratek, 10 úvod,
11–12 kapitola 1, 13 kapitola 2 (obrázek, tabulka), 14 rovnice a výčty,
15 závěr, 16 seznam literatury, 17 přílohy.

`rozhodnutí repa` — pravidlo nebo varianta, kterou zdroje neuvádějí, ale repo ji přijímá z praktických důvodů: písmo **Carlito** jako náhrada Calibri / Calibri Light (Calibri není volně šiřitelné, v CI ho mít nelze; Carlito má stejné rozměry znaků) a některé chyby LaTeXu v [latex-chyby.md](latex-chyby.md), které Word nedělá.

Témata semináře: `Úvod`, `Závěr`, `Abstrakt`, `Typy BP` (implementační, návrhová,
srovnávací a kombinovaná práce), `Rešerše`, `Citace`, `Typografie`, `Chyby`
(nejčastější chyby v pracích), `Vyhledávání` (klíčová slova). Materiály semináře
**nejsou v repu** (patří vyučujícím); které soubory se použily, je v
[pokryti.md](pokryti.md). Pravidla, jejichž jediným zdrojem je `seminář …`, jsou
**doporučení Katedry technických studií** — kontrola je hlásí jako upozornění,
ne jako chybu.

Z APA manuálu se přebírají jen citace; jeho úprava obrázků, grafů a tabulek
(Times New Roman 12, název nad obrázkem) odporuje šabloně VŠPJ a nepoužívá se.

Export z LibreOffice se jako zdroj nepoužívá — šablonu vykresluje jinak
(viz [Dokumenty/README.MD](../../Dokumenty/README.MD)).

### Kde získat aktuální zdroje

Aktuální verze příručky i šablony zveřejňuje VŠPJ na:

- https://kts.vspj.cz/cs/statni-zaverecne-zkousky/zaverecne-prace
- https://is.vspj.cz/dokumentace-student/

Když vyjde nová verze, aktualizuj soubory v `Dokumenty/`, znovu vyexportuj
`Sablona.pdf` z Wordu (Word Online → Stáhnout jako PDF) a projdi pravidla,
která se na změněné části odkazují.

## Soubory

| Soubor | Prefix | | Soubor | Prefix |
|---|---|---|---|---|
| [dokument.md](dokument.md) — celý dokument | DOK | | [prvky/nadpis-1.md](prvky/nadpis-1.md) | NA1 |
| [stranky/titulni-strana.md](stranky/titulni-strana.md) | TIT | | [prvky/nadpis-2.md](prvky/nadpis-2.md) | NA2 |
| [stranky/zadani.md](stranky/zadani.md) | ZAD | | [prvky/nadpis-3.md](prvky/nadpis-3.md) | NA3 |
| [stranky/abstrakt.md](stranky/abstrakt.md) | ABS | | [prvky/obrazek.md](prvky/obrazek.md) | OBR |
| [stranky/prohlaseni.md](stranky/prohlaseni.md) | PRO | | [prvky/tabulka.md](prvky/tabulka.md) | TAB |
| [stranky/podekovani.md](stranky/podekovani.md) | POD | | [prvky/rovnice.md](prvky/rovnice.md) | ROV |
| [stranky/obsah.md](stranky/obsah.md) | OBS | | [prvky/vycet-seznam.md](prvky/vycet-seznam.md) | VYC |
| [stranky/seznam-obrazku.md](stranky/seznam-obrazku.md) | SOB | | [prvky/odkaz-v-textu.md](prvky/odkaz-v-textu.md) | CIT |
| [stranky/seznam-tabulek.md](stranky/seznam-tabulek.md) | STA | | [prvky/poznamka-pod-carou.md](prvky/poznamka-pod-carou.md) | PPC |
| [stranky/seznam-zkratek.md](stranky/seznam-zkratek.md) | SZK | | [prvky/polozka-literatury.md](prvky/polozka-literatury.md) | BIB |
| [stranky/uvod.md](stranky/uvod.md) | UVO | | | |
| [stranky/kapitola.md](stranky/kapitola.md) — běžná kapitola | KAP | | | |
| [stranky/zaver.md](stranky/zaver.md) | ZAV | | | |
| [stranky/seznam-literatury.md](stranky/seznam-literatury.md) | LIT | | | |
| [stranky/prilohy.md](stranky/prilohy.md) | PRI | | [latex-chyby.md](latex-chyby.md) — typické chyby LaTeXu | LTX |

[pokryti.md](pokryti.md) — které pravidlo pokrývá kterou kapitolu příručky,
styl, oddíl a pokyn šablony.

Pravidlo platné pro víc typů je zapsané jednou (u nejobecnějšího typu,
většinou v `dokument.md`) a ostatní na něj odkazují `viz DOK-F04`.

## Formát pravidla

```markdown
### OBR-F03 Titulek pod obrázkem
- Pravidlo: Titulek je pod obrázkem, Calibri 10 pt, tučně, na střed, mezera za 0 pt.
- Zdroj: šablona styl Titulek; příručka 3, 6.2
- Varianty: —
- Ověření: PDF — řádek pod obrázkem, výška písma ≈ 10 pt, tučný, na střed
- Štítky: obrázek, titulek, písmo, zarovnání, měření
- Poznámka: (volitelné) proč pravidlo vypadá tak, jak vypadá
```

- **ID** `PREFIX-F01` (formální) nebo `PREFIX-O01` (obsahová), čísla 01–99
  v každé řadě. ID se nepřečíslovávají; smazané ID se znovu nepoužije.
- **Pravidlo** — jedna věta (nebo pár vět), hodnoty v pt s desetinnou čárkou.
- **Zdroj** — jeden nebo víc odkazů oddělených středníkem ve tvarech z tabulky
  Zdroje; může následovat poznámka v závorce, např. `příručka 3 (Tab. 1)`,
  `Word PDF s. 1 (změřeno)`. Odkaz na jiné pravidlo: `viz DOK-F04`.
- **Varianty** — `—`, nebo seznam variant, když si zdroje odporují (viz níže).
- **Ověření** — `PDF — …`, `zdroj — …` nebo `PDF + zdroj — …` a co se hledá.
  `zdroj` = jde ověřit jen ze zdrojového souboru práce (DOCX/.tex), např.
  použití stylu. Tolerance jsou orientační; definitivní určí kontrolní skill.
- **Štítky** — čeho se pravidlo týká a jak se ověřuje, ze slovníku níže
  (oddělené čárkou, aspoň jeden štítek „jak“). Slouží k seskupení kontrol
  a ke konkrétnějšímu hlášení u pravidel, která pokrývají víc věcí najednou.
- **Poznámka** — volitelné vysvětlení.

### Štítky

| Skupina | Štítky |
|---|---|
| Co — vzhled | písmo, barva, zarovnání, řádkování, mezery, odsazení, poloha, jednotnost |
| Co — stránky a struktura | stránkování, číslování-stránek, záhlaví, struktura |
| Co — prvky | nadpis, titulek, zdroj, obrázek, tabulka, rovnice, výčet, poznámka, číslování |
| Co — sazba textu | interpunkce, uvozovky, pomlčky, pevné-mezery, dělení-slov, čísla-a-jednotky, zkratky |
| Co — citace a obsah | citace, literatura, obsah-textu, styl (odborný styl textu), latex |
| Jak se ověřuje | **měření** (geometrie z PDF), **text** (text vytažený z PDF), **posouzení** (úsudek čtenáře / modelu), **zdrojový-soubor** (.tex, DOCX, log) |

Seznam je v `kontrola.py` (`STITKY_CO`, `STITKY_JAK`); nový štítek se přidává tam i sem.

Každý soubor stránky a prvku má na začátku sekci `## Rozpoznání` — podle čeho
kontrola stránku nebo prvek v PDF najde. Pořadí částí práce je pevné
(DOK-F17), takže úvodní strany mají pevnou fyzickou stranu (1 titulní,
2 zadání, 3 abstrakt, 4 prohlášení, 5 poděkování — nepovinné) a další části
se poznají podle nadpisu 1. úrovně.

Každý soubor má sekce `## Formální` (řezy, velikosti, mezery, polohy,
číslování) a `## Obsahová` (co má část obsahovat). Obsahová kategorie se bude
doplňovat z dalších materiálů; zatím obsahuje jen to, co zdroje výslovně říkají.

Pravidla se netýkají konkrétního textu (jméno autora, název práce) — jen
formátu a pevných textů (nadpisy „Abstrakt“, „Úvod“, „Bakalářská práce“…).

## Varianty

Když si zdroje odporují (příručka × šablona DOCX × Word PDF), pravidlo uvede
všechny varianty, každou se zdrojem:

```markdown
- Varianty:
  - a) na střed — příručka 3 (Tab. 1)
  - b) vlevo — šablona styl Nadpis 1; Word PDF s. 11
```

Při kontrole **vyhovuje kterákoli varianta**; kontrola jen poznamená, že se
zdroje rozcházejí. Za chybu se považuje až stav, který neodpovídá žádné.

## Nepopsané prvky

Pravidla pokrývají jen to, co popisují zdroje. V práci se mohou objevit prvky,
pro které pravidlo není. Kontrola je v tom případě **nehodnotí jako chybu**:
uvede, že prvek našla, že pro jeho formát nemá pravidlo, a upozorní, že si
jeho úpravou není jistá. Až se takový prvek objeví v praxi, doplní se sem
pravidlo.

Známé nepopsané prvky:

- výpis zdrojového kódu (v textu i v přílohách),
- tabulka přes více stránek (opakované záhlaví, pokračování titulku),
- stránka na šířku,
- víceřádkový titulek obrázku nebo tabulky (zarovnání dalších řádků),
- obrázek složený z více částí (a), b)…),
- URL a e-mailové adresy v běžném textu (písmo, zalomení),
- obrázky a tabulky v přílohách (číslování, zda patří do seznamů),
- čtvrtá a další úroveň výčtu,
- celkový rozsah práce — požadavky nejsou v dostupných zdrojích; kontrola rozsah jen změří a uvede (DOK-F20).

## Převody jednotek (DOCX)

| DOCX | pt |
|---|---|
| twips (`w:spacing`, `w:ind`, okraje) | twips / 20 |
| `w:sz` (půlbody) | sz / 2 |
| `w:line` při `lineRule="auto"` | line / 240 = násobek řádkování (276 → 1,15) |
| cm | cm × 28,3465 |

## Rozpory

Místa, kde si zdroje odporují. Pravidla v posledním sloupci uvádějí všechny
varianty; při kontrole vyhovuje kterákoli z nich.

| Téma | Příručka | Šablona DOCX / Word PDF | Pravidla |
|---|---|---|---|
| Zarovnání Nadpisu 1 | na střed (Tab. 1) | vlevo (styl i PDF; kopie Tab. 1 v šabloně uvádí na střed) | NA1-F02 |
| Text v tabulce | 11/10 pt, na střed | styl Tabulka 10 pt, vlevo | TAB-F04 |
| Řádkování v tabulce | 1 | styl Tabulka 1; vzorová tabulka 1,15 | TAB-F05 |
| Označení příloh | „Příloha 1, 2…“ | „Příloha A.1, B.2…“ | PRI-F02 |
| Číslování stránek příloh | nečíslují se | „nemusí se číslovat v návaznosti“ | PRI-F03 |
| Tučné v textu | nepoužívá se | „omezeně lze“ | DOK-F12 |
| Zdroj pod obrázkem | „zdroj:“ (příklad) | „Zdroj:“ | OBR-F04 |
| První číslovaná strana | Obsah (zpravidla 6) | pole PAGE až od Úvodu (oddíl 6) | DOK-F09 |
| Dělení slov | nutné u zarovnání do bloku | šablona automatické dělení nemá | DOK-F10 |
| Předsazení položek literatury | styl Bibliografie s předsazením (kap. 3) × styl Normální (kap. 7.1) | styl Seznam literatury s předsazením | BIB-F02 |
| Umístění seznamů obrázků a tabulek | za obsahem, nebo před literaturou | za obsahem | DOK-F17 |
| Druhý řádek titulní strany | studijní obor | Studijní program | TIT-O01 |
| Rok na titulní straně | rok obhajoby | pole TIME (aktuální rok) | TIT-O02 |
| Řádkování poznámek pod čarou | jako základní text (1,15, za 6 pt) | styl Text poznámky pod čarou: 1, za 0 | PPC-F02 |
| Mezera před „Abstract“ | bez prázdných odstavců | prázdný odstavec mezi českou a anglickou částí | ABS-F03 |
| Písmo | Calibri / Calibri Light | Calibri / Calibri Light; repo přijímá Carlito (rozhodnutí repa) | DOK-F03, DOK-F04 |

Rozpory s materiály semináře a s APA (citace podle APA jsou rovnocenná varianta):

| Téma | Varianty a zdroje | Pravidla |
|---|---|---|
| Délka abstraktu | ≤ 150 slov (šablona) × 8–10 řádků (seminář) × ≤ 250 slov (norma podle semináře) | ABS-O01 |
| Délka závěru | ≤ 2 strany × 2–3 strany (oba seminář) | ZAV-O09 |
| Citační systém | šablona 2023: „povolen pouze harvardský styl“ × APA manuál (Ústav pedagogických věd) — APA přijato rozhodnutím uživatele | CIT-F01 |
| Odkaz v textu | „s.“ a „a“ (příručka) × „str.“ a „&“ (seminář) × APA | CIT-F01 |
| Více autorů | „a kol.“ od 4 autorů (příručka) × „et al.“ od 3 (APA) | CIT-F03 |
| Zdroj bez data | „nedatováno“ (příručka) × „n.d.“ (APA) | CIT-F04 |
| Přímá citace | uvozovky nebo kurzíva (příručka) × uvozovky bez kurzívy, blok nad 40 slov (APA) | CIT-F05 |
| Tvar položky literatury | ČSN ISO 690 (příručka) × APA | BIB-F03 |
| Autoři v seznamu literatury | všichni nebo „a kol.“ (příručka) × všichni do 20 (APA) | BIB-O01 |
| Dělení slov | nutné (příručka) × raději nedělit (seminář Typografie, šablona) | DOK-F10 |

Nejsou to rozpory zdrojů, ale stojí za zmínku:

- **Poděkování dole na stránce** (POD-F02) — oddíl šablony má svislé zarovnání
  dolů a Word PDF ho tak vykresluje; jen LibreOffice ho dá nahoru (LibreOffice
  není zdroj).
- **Název stylu literatury** — příručka „Bibliografie“, šablona „Seznam
  literatury“; tentýž styl (BIB-F01).
- **Záhlaví mimo střed** — středový tabulátor záhlaví je o ≈ 14 pt vpravo od
  středu textu (DOK-F08).
- **Starší šablona v semináři** — prezentace Typografie uvádí „šablonu VŠPJ“
  s Times New Roman 12, řádkováním 1,5 a mezerou 9 b. Jde o starší verzi;
  platí šablona 2023. Podobně prezentace Jak psát závěr cituje starší znění
  pokynu k závěru (ZAV-O03) a soubor prohlášení v semináři je starší znění.
- **Typ práce na titulní straně** — ve Word PDF je zástupný text 11 pt,
  vyplněná hodnota má 14 pt; řádky pod ním se mohou posunout až o ≈ 3,7 pt
  (odhad, neměřeno; TIT-F06).

## Kontrola formátu

```sh
python3 docs/pravidla/kontrola.py           # formát existujících souborů
python3 docs/pravidla/kontrola.py --uplne   # + všechny soubory, odkazy, rozpory, pokrytí
python3 -m pytest -q docs/pravidla          # testy kontrolního skriptu
```

Skript kontroluje jen formu (ID, pole, tvar zdrojů, odkazy), ne správnost pravidel.
