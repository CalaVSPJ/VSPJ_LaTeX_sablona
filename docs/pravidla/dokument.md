# Celý dokument

Pravidla, která platí pro celou práci. Ostatní soubory na ně odkazují `viz DOK-NN`
a nezapisují je znovu.

## Formální

### DOK-F01 Papír a tisk
- Pravidlo: Práce je ve formátu A4 (210 × 297 mm, 595,3 × 841,9 pt), na výšku, určená k jednostrannému tisku a vazbě.
- Zdroj: příručka 10; šablona oddíl 1; šablona pokyn v Úvodu
- Varianty: —
- Ověření: PDF — rozměr každé stránky 595,3 × 841,9 pt (±1 pt), orientace na výšku
- Štítky: stránkování, měření
- Poznámka: Příručka připouští oboustranný tisk, ale doporučuje jednostranný; šablona počítá s jednostranným (stejné okraje na všech stránkách).

### DOK-F02 Okraje
- Pravidlo: Okraje jsou nahoře 2,5 cm (70,9 pt), dole 2,5 cm, vlevo 3,5 cm (99,25 pt, včetně 1 cm na vazbu), vpravo 2,5 cm; šířka textu 15,0 cm (425,15 pt). Stejné na všech stránkách.
- Zdroj: příručka 10; šablona oddíl 1; šablona pokyn v Úvodu; Word PDF s. 10 (změřeno)
- Varianty: —
- Ověření: PDF — levá hrana textu ≈ 99,5 pt, pravá hrana textu zarovnaného do bloku ≈ 523,5 pt, žádný text (kromě záhlaví a čísla stránky) nad 70,9 pt ani pod 771 pt
- Štítky: poloha, měření
- Poznámka: Příručka mluví o „vnitřním“ a „vnějším“ okraji; při jednostranném tisku je vnitřní okraj vždy vlevo.

### DOK-F03 Základní písmo
- Pravidlo: Základní text, titulky, zdroje, tabulky, poznámky pod čarou, záhlaví i číslo stránky jsou v písmu Calibri; základní text má 11 pt.
- Zdroj: příručka 2, 3; šablona styl Normální; šablona pokyn v Úvodu
- Varianty:
  - a) Calibri — šablona styl Normální; příručka 3
  - b) Carlito (metricky shodná náhrada Calibri) — rozhodnutí repa (README)
- Ověření: PDF — názvy písem vložených v PDF (pdffonts), výška písma základního textu 11 pt
- Štítky: písmo, měření, zdrojový-soubor
- Poznámka: Calibri není volně šiřitelné, proto se v LaTeXu a v CI používá Carlito se stejnými rozměry znaků. Varianta b) není ve zdrojích, je to rozhodnutí repa (viz README, Zdroje).

### DOK-F04 Písmo nadpisů a počet typů písma
- Pravidlo: Nadpisy (Nadpis 1–3, Název) a texty titulní strany jsou v písmu Calibri Light; v práci se nekombinují více než dva typy písma (jeden pro nadpisy, druhý pro vše ostatní).
- Zdroj: příručka 2, 3; šablona styl Nadpis 1; šablona titulní strana; šablona pokyn v Přílohách
- Varianty:
  - a) Calibri Light — šablona styl Nadpis 1; příručka 3
  - b) Carlito v náhradě za Calibri Light (běžný řez Carlito s mírně dopočtenou tučností, protože Calibri Light tučný řez nemá) — rozhodnutí repa (README)
- Ověření: PDF — v PDF jsou nejvýš dvě rodiny písma (+ matematické písmo rovnic), nadpisy mají jinou rodinu nebo řez než základní text
- Štítky: písmo, nadpis, jednotnost, měření, zdrojový-soubor
- Poznámka: Calibri Light nemá tučný řez, Word tučnost dopočítá — výsledek vypadá jako běžné Calibri. Šablona v pokynu u příloh píše „Pro celou práci se použije jeden typ písma“; myslí se tím jednotnost, ne zákaz písma nadpisů.

### DOK-F05 Základní odstavec
- Pravidlo: Odstavec základního textu je zarovnaný do bloku, řádkování 1,15 (rozteč řádků ≈ 15,4 pt), mezera před 0 pt, za odstavcem 6 pt, bez odsazení prvního řádku; odstavce se oddělují jen mezerou za odstavcem.
- Zdroj: příručka 1.1, 1.2, 3; šablona styl Normální; šablona pokyn v Úvodu; Word PDF s. 13 (změřeno)
- Varianty: —
- Ověření: PDF — rozteč řádků uvnitř odstavce ≈ 15,4 pt (±0,5), mezi odstavci ≈ 21,4 pt, první řádek odstavce začíná na levém okraji, řádky kromě posledního sahají k pravému okraji
- Štítky: zarovnání, řádkování, mezery, odsazení, měření
- Poznámka: Příručka 1.2: velikost mezery se odvozuje od velikosti písma (celá nebo polovina) — 6 pt ≈ polovina 11 pt.

### DOK-F06 Žádné prázdné odstavce
- Pravidlo: Mezery mezi odstavci ani posun textu na další stránku se nedělají prázdnými odstavci (prázdnými řádky); nová stránka se začíná zalomením stránky, mezery nastavením odstavce.
- Zdroj: příručka 1, 1.2
- Varianty: —
- Ověření: PDF + zdroj — v PDF žádná mezera mezi odstavci textu větší než ≈ 1 řádek bez důvodu (nadpis, obrázek, tabulka) a žádný začátek stránky posunutý dolů; ve zdroji žádné prázdné odstavce / `\\` / `\vspace` v textu
- Štítky: mezery, stránkování, měření, zdrojový-soubor
- Poznámka: Šablona prázdné odstavce sama používá na titulní straně (rozvržení), na straně Abstraktu mezi českou a anglickou částí (viz ABS-F03) a v prohlášení před podpisem; Poděkování je dole na stránce záměrně (POD-F02). Tato místa nejsou porušením pravidla.

### DOK-F07 Sirotci a vdovy
- Pravidlo: Poslední řádek odstavce nesmí být sám na začátku stránky (sirotek — hrubá chyba); první řádek odstavce nemá zůstat sám na konci stránky (vdova — v odůvodněných případech tolerována). Odstavec kratší než 4 řádky se mezi stránky nedělí.
- Zdroj: příručka 1.3; šablona styl Normální (kontrola osamocených řádků zapnuta)
- Varianty: —
- Ověření: PDF — první řádek stránky není neúplný poslední řádek odstavce; poslední řádek stránky není první řádek odstavce, po kterém odstavec pokračuje
- Štítky: stránkování, měření
- Poznámka: Příručka definuje sirotka a vdovu obráceně než část literatury; pravidlo zakazuje oba případy, takže na pojmenování nezáleží.

### DOK-F08 Záhlaví
- Pravidlo: Od stránky Obsah do konce práce (včetně příloh) je v záhlaví text „Vysoká škola polytechnická Jihlava“ v písmu Calibri 11 pt, kurzívou, šedou barvou (#808080), na středovém tabulátoru (střed textu ≈ 226,8 pt od levého okraje textu), 1,25 cm od horní hrany papíru. Titulní strana, zadání, abstrakt, prohlášení a poděkování záhlaví nemají.
- Zdroj: šablona oddíl 4; šablona oddíl 1; Word PDF s. 6 (změřeno); Word PDF s. 17
- Varianty: —
- Ověření: PDF — na stránkách od Obsahu řádek záhlaví s inkoustem ≈ 38,5–48 pt, střed ≈ 326 pt (±8), šedý kurzívní text; na stránkách 1–5 nic nad 70 pt
- Štítky: záhlaví, písmo, barva, poloha, měření
- Poznámka: Středový tabulátor stylu Záhlaví je o ≈ 14 pt vpravo od středu textové plochy (311,6 pt); záhlaví vycentrované přesně na střed textu se od Wordu viditelně liší.

### DOK-F09 Číslování stránek
- Pravidlo: Stránky se počítají od titulní strany (titulní = 1). Číslo stránky je v zápatí vpravo (u pravého okraje textu), arabskými číslicemi, Calibri 11 pt, bez celkového počtu stran, spodní hrana ≈ 38 pt nad dolní hranou papíru. Úvodní stránky (titulní, zadání, abstrakt, prohlášení, poděkování) číslo nemají; číslování příloh viz PRI-F03.
- Zdroj: příručka 12, 13; šablona oddíl 6; Word PDF s. 10 (změřeno)
- Varianty:
  - a) číslo se zobrazuje od Obsahu (zpravidla strana 6) po Seznam použité literatury — příručka 12
  - b) číslo se zobrazuje až od Úvodu po Seznam použité literatury; Obsah a seznamy bez čísla — šablona oddíl 6; Word PDF s. 6 (bez čísla)
- Ověření: PDF — tištěné číslo = fyzické pořadí stránky v PDF; číslo vpravo dole (pravá hrana ≈ 523,5 pt, inkoust ≈ 796–804 pt); stránky 1–5 bez čísla
- Štítky: číslování-stránek, poloha, měření, text
- Poznámka: Čísla příloh viz PRI (příručka a šablona se liší i tam).

### DOK-F10 Dělení slov
- Pravidlo: Text zarovnaný do bloku se dělí podle pravidel pravopisu: na konci řádku nezůstane jedno písmeno, na další řádek nepřejdou jen dvě písmena, nedělí se poslední slovo odstavce ani poslední slovo na stránce. Text zarovnaný vlevo (tabulky, literatura) a titulky se nedělí.
- Zdroj: příručka 4.5, 6.1, 6.2
- Varianty:
  - a) slova se dělí — příručka 4.5
  - b) slova se nedělí (šablona nemá zapnuté automatické dělení slov; seminář: „pokud nemusíte, dělení slov nepoužívejte“) — šablona nastavení dokumentu; Word PDF s. 13; seminář Typografie
- Ověření: PDF — u dělených slov: před spojovníkem na konci řádku aspoň 2 písmena, za ním aspoň 3; poslední řádek odstavce a poslední řádek stránky nekončí spojovníkem dělení
- Štítky: dělení-slov, text
- Poznámka: Bez dělení vznikají v textu do bloku velké mezery mezi slovy; příručka dělení výslovně vyžaduje.

### DOK-F11 Pevné mezery a jednopísmenné předložky
- Pravidlo: Jednopísmenné předložky a spojky (k, s, v, z, o, u, i, a) nesmí být na konci řádku (u spojky „a“ jsou výjimky). Na jednom řádku musí zůstat: číslo a jednotka (200 Kč, 80 mm), vícemístné číslo (15 000), datum (1. 7. 1998), titul a jméno, zkratka jména a příjmení (J. Drda), telefonní číslo.
- Zdroj: příručka 4, 4.5
- Varianty: —
- Ověření: PDF — žádný řádek textu nekončí jednopísmenným slovem k/s/v/z/o/u/i (a); žádný řádek nekončí číslem, po kterém na dalším řádku následuje jednotka nebo další skupina číslic
- Štítky: pevné-mezery, text
- Poznámka: Spojka „a“ na konci řádku je přípustná výjimka — kontrola ji hlásí jen jako upozornění.

### DOK-F12 Zvýrazňování a barva textu
- Pravidlo: Důležitá slova a přímé citace se zvýrazňují kurzívou. Nepoužívá se podtržení, prostrkání ani barevné zvýraznění; text je černý (kromě šedého záhlaví).
- Zdroj: příručka 2; šablona pokyn v Úvodu
- Varianty:
  - a) tučné písmo se v textu nepoužívá — příručka 2
  - b) tučné písmo lze omezeně použít — šablona pokyn v Úvodu
- Ověření: PDF — v základním textu žádné podtržení (čáry pod textem mimo tabulky), žádný barevný text (mimo záhlaví a obrázky); počet tučných úseků v odstavcích textu
- Štítky: písmo, barva, měření, posouzení
- Poznámka: Prohlášení má v pevném znění šablony tučně „AZ“ a „souhlasím“ (viz PRO-F03); to není zvýrazňování v textu práce.

### DOK-F13 Interpunkce a speciální znaky
- Pravidlo: Interpunkční znaménka se píší těsně za slovo a od dalšího slova se oddělují mezerou. Za nadpisem a titulkem se tečka nepíše. Uvozovky jsou české „…“ těsně k uvozenému textu; závorky bez mezer uvnitř. Spojovník (-) je bez mezer (e-mail), pomlčka (–) jako náhrada „až/versus“ bez mezer (8–20 h, 1598–1649), v jiném významu s mezerami; pomlčka nezačíná řádek. Trojtečka je jeden znak (…). Znaky násobení, dělení a poměru se oddělují mezerami (3 · 6, 6 : 3); skóre a čas bez mezer (2:3).
- Zdroj: příručka 4.1, 4.2, 4.3, 4.4
- Varianty: —
- Ověření: PDF — text: žádné "…" anglické uvozovky ani ″, žádné „...“ ze tří teček, žádná mezera před , . ; : ? ! ani uvnitř závorek, rozsahy číslic s pomlčkou (ne spojovníkem), žádný řádek nezačíná pomlčkou
- Štítky: interpunkce, uvozovky, pomlčky, text
- Poznámka: Příklady v příručce používají znak − (minus) jako pomlčku; v kontrole se jako pomlčka přijímá – (U+2013) i − (U+2212).

### DOK-F14 Čísla, jednotky a značky
- Pravidlo: Jednotka se od čísla odděluje pevnou mezerou (10 m, 25 %, 10 °C); bez mezery jen ve významu přídavného jména (15% roztok, 12° pivo). Víceciferná čísla se dělí do skupin po třech mezerou (7 000). Desetinná čárka bez mezery. Datum s mezerami (1. 7. 1998), letopočet celý. § se píše bez tečky a od čísla se odděluje zúženou mezerou.
- Zdroj: příručka 4.4, 4.5
- Varianty: —
- Ověření: PDF — text: číslo těsně následované %, °C, Kč, m, mm, kg bez mezery hlásit k posouzení; datum ve tvaru 1.7.1998 bez mezer hlásit
- Štítky: čísla-a-jednotky, pevné-mezery, text
- Poznámka: Nižší čísla se v textu vyjadřují slovy — viz DOK-O02.

### DOK-F15 Kapitola na nové stránce
- Pravidlo: Každý nadpis 1. úrovně (kapitola i nečíslované části Úvod, Závěr, Seznam použité literatury, Přílohy, seznamy) a každá úvodní stránka (zadání, abstrakt, prohlášení, poděkování, obsah) začíná na nové stránce.
- Zdroj: šablona styl Nadpis 1 (vložit konec stránky před); šablona oddíl 1; šablona oddíl 2; šablona oddíl 3; šablona oddíl 4; šablona pokyn v Úvodu
- Varianty: —
- Ověření: PDF — každý nadpis 1. úrovně je první řádek textu na stránce (pod záhlavím)
- Štítky: stránkování, nadpis, měření

### DOK-F16 Nejvýše tři úrovně nadpisů
- Pravidlo: Práce používá nejvýše tři úrovně nadpisů (Nadpis 1, 2, 3) s desetinným číslováním 1, 1.1, 1.1.1.
- Zdroj: příručka 3, 5, 5.1; šablona pokyn v kapitole 1
- Varianty: —
- Ověření: PDF — žádné číslo nadpisu se čtyřmi úrovněmi (1.1.1.1); zdroj — jen styly Nadpis 1–3 / `\chapter`, `\section`, `\subsection`
- Štítky: nadpis, číslování, struktura, text, zdrojový-soubor

### DOK-F17 Pořadí částí práce
- Pravidlo: Práce má části v tomto pořadí: titulní strana, zadání, abstrakt (s klíčovými slovy, Abstract a Keywords), prohlášení, poděkování (nepovinné), obsah, seznam obrázků, seznam tabulek, seznam zkratek (každý jen když je potřeba), úvod, kapitoly, závěr, seznam použité literatury, přílohy (nepovinné).
- Zdroj: šablona oddíl 1; příručka 12, 13, 7.1
- Varianty:
  - a) seznamy obrázků a tabulek za obsahem — šablona oddíl 5; příručka 6.3
  - b) seznamy obrázků a tabulek před seznamem použité literatury — příručka 6.3
- Ověření: PDF — pořadí nadpisů stránek odpovídá výčtu (vynechané nepovinné části nevadí)
- Štítky: struktura, stránkování, text
- Poznámka: Příručka 12 vyjmenovává úvodní stránky jako „titulní stránka, zadání, anotace, čestné prohlášení, poděkování“ — anotace = abstrakt.

### DOK-F18 Jednotná úprava
- Pravidlo: Významově stejné prvky (text, nadpisy stejné úrovně, titulky, tabulky, výčty, grafy) mají v celé práci stejné písmo, velikost, řez, řádkování a mezery.
- Zdroj: příručka 2, 5.2, 6.1, 6.2
- Varianty: —
- Ověření: PDF — u všech výskytů téhož prvku stejná výška písma, řez a mezery (±0,5 pt)
- Štítky: jednotnost, měření

### DOK-F19 Bez pokynů a vzorového textu šablony
- Pravidlo: V odevzdané práci nezůstanou pokyny šablony (modrý a šedý vysvětlující text), zástupný text polí („Zvolte položku.“, „Klikněte nebo klepněte sem…“) ani výplňový vzorový text šablony. Platí pro všechny stránky.
- Zdroj: šablona pokyn v Úvodu; šablona pokyn na straně Zadání
- Varianty: —
- Ověření: PDF — žádný barevný text mimo záhlaví a obrázky; žádná z vět pokynů šablony ani vzorové věty typu „Vlastní text kapitoly.“
- Štítky: barva, obsah-textu, text, měření
- Poznámka: Šablona to neříká jednou větou, vyplývá to z povahy pokynů („Tato šablona slouží jako šablona…“, „Místo této stránky vložte…“).

### DOK-F20 Rozsah práce
- Pravidlo: Celkový rozsah práce zdroje neuvádějí. Kontrola rozsah vždy změří a uvede: vlastní text = stránky od nadpisu „Úvod“ po konec Závěru včetně (bez úvodních stran, obsahu, seznamů, literatury a příloh); uvede počet stran, slov a normostran (1 800 znaků včetně mezer). Pokud zadání (strana 2) rozsah uvádí, porovná ho; jinak napíše, že požadovaný rozsah nezná, a rozsah nehodnotí.
- Zdroj: rozhodnutí repa
- Varianty: —
- Ověření: PDF — změřit stránky Úvod–Závěr, počet slov a znaků; hledat v zadání údaj o rozsahu („rozsah“, „stran“, „normostran“)
- Štítky: struktura, měření, text
- Poznámka: Materiály semináře zmiňují mezi chybami „počet znaků na řádku a počet řádků na stránce neodpovídá požadavkům“ — požadavky samotné ale v dostupných zdrojích nejsou. Až se najdou, doplní se sem jako hodnota.

## Obsahová

Účel: Pravidla pro text celé práce — odborný styl, jazyková správnost,
soulad práce se zadáním a ochrana údajů.

### DOK-O01 Zkratky
- Pravidlo: Zkratky se používají jen u vžitých výrazů a nezůstávají nevysvětlené. Pokud práce nemá seznam zkratek, uvede se při prvním použití celý název a zkratka v závorce, např. Vysoká škola polytechnická Jihlava (VŠPJ).
- Zdroj: příručka 4.5; seminář Chyby
- Varianty: —
- Ověření: PDF — první výskyt každé zkratky z velkých písmen (bez seznamu zkratek) je v závorce za celým názvem
- Štítky: zkratky, text

### DOK-O02 Čísla slovy
- Pravidlo: Nižší číselné údaje se v textu vyjadřují slovy, víceciferná čísla lze číslicemi; oba způsoby se nekombinují (ne „2 tisíce“, „6 mil. 576 tis.“). Výjimkou jsou letopočty, data, čísla s jednotkami, zápis velkých čísel se zkratkou řádu („10 mil.“) a složeniny čísla se slovem („16krát“, „8bitový“).
- Zdroj: příručka 4.5; seminář Typografie
- Varianty: —
- Ověření: PDF — číslice 1–9 samostatně v textu bez jednotky hlásit k posouzení
- Štítky: čísla-a-jednotky, text, posouzení

### DOK-O03 Skladba kapitol
- Pravidlo: Skladba a názvy kapitol (Teoretická část, Praktická část…) jsou doporučené; podle tématu a zvyklostí katedry mohou být upraveny. Povinné jsou úvodní stránky, úvod, závěr a seznam použité literatury.
- Zdroj: šablona pokyn v Úvodu; viz DOK-F17
- Varianty: —
- Ověření: PDF — kontroluje se jen přítomnost povinných částí, ne názvy kapitol textu
- Štítky: struktura, posouzení

### DOK-O04 Odborný styl — bez první osoby
- Pravidlo: Práce je psaná odborným stylem, ne v první osobě (jednotného ani množného čísla), pokud to není opodstatněné (výjimkou je vysvětlení motivace v úvodu, viz UVO-O09).
- Zdroj: seminář Úvod
- Varianty: —
- Ověření: PDF — tvary „já“, „jsem udělal“, „myslím si“, „můj“, „jsme zjistili“, „naše aplikace“ mimo pasáž o motivaci v úvodu → upozornění
- Štítky: styl, obsah-textu, text

### DOK-O05 Odborný styl — výrazivo
- Pravidlo: Text používá přesné a jednoznačné odborné výrazy; nepoužívá hovorová ani citově zabarvená (příznaková) slova, novinářský ani marketingový styl, zbytečně neopakuje stejné informace ani stejná slova (kromě odborných termínů) a nejednoznačná vyjádření přeformuluje.
- Zdroj: seminář Úvod; seminář Závěr; seminář Abstrakt
- Varianty: —
- Ověření: PDF — posouzení: hovorové výrazy, superlativy a reklamní formulace („úžasný“, „super“, „naprosto skvělé“), vykřičníky, opakované věty → upozornění
- Štítky: styl, obsah-textu, posouzení

### DOK-O06 Název, obsah a zadání
- Pravidlo: Název práce odpovídá jejímu obsahu, obsah odpovídá zadání a práce řeší zadaný úkol.
- Zdroj: seminář Chyby; seminář Úvod
- Varianty: —
- Ověření: PDF — posouzení: název (titulní strana), zadání (s. 2), cíl v úvodu a obsah kapitol popisují tutéž věc
- Štítky: obsah-textu, struktura, posouzení

### DOK-O07 Odborné termíny
- Pravidlo: Práce používá správné odborné termíny, v celé práci jednotně (tentýž pojem stejným výrazem).
- Zdroj: seminář Chyby; seminář Abstrakt
- Varianty: —
- Ověření: PDF — posouzení: pro tentýž pojem střídání více výrazů nebo zjevně nesprávný termín → upozornění
- Štítky: styl, obsah-textu, jednotnost, posouzení

### DOK-O08 Věta nezačíná číslicí
- Pravidlo: Věta nezačíná číslicí — „Dne 17. listopadu…“, „Pětihodinový maraton…“, ne „17. listopadu…“, „5hodinový maraton…“.
- Zdroj: seminář Typografie
- Varianty: —
- Ověření: PDF — začátek odstavce nebo začátek věty (po „.“, „?“, „!“ a mezeře) nezačíná číslicí; za konec věty se **nepočítá** tečka za zkratkou (s., str., obr., tab., kap., č., tj., např.), za řadovou číslovkou nebo uvnitř data („2. 10. 2020“) a odkazy v závorkách
- Štítky: styl, čísla-a-jednotky, text

### DOK-O09 Jazyková správnost
- Pravidlo: Práce je bez gramatických chyb a překlepů; za jazykovou správnost odpovídá student.
- Zdroj: seminář Typografie; seminář Chyby; seminář Úvod
- Varianty: —
- Ověření: PDF — kontrola pravopisu a překlepů v textu (mimo citace a kód)
- Štítky: styl, obsah-textu, text

### DOK-O10 Bez citlivých osobních údajů
- Pravidlo: Práce neobsahuje citlivé osobní údaje — závěrečné práce se zveřejňují.
- Zdroj: směrnice SP 2/2020 (čl. 3); směrnice SP 2/2020 (čl. 6)
- Varianty: —
- Ověření: PDF — posouzení: údaje o zdraví, původu, víře, politických názorech nebo sexuální orientaci konkrétních identifikovatelných osob (např. jmenovaných respondentů) → upozornění
- Štítky: obsah-textu, text, posouzení

