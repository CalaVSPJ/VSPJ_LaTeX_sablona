# Typické chyby LaTeXu

Chyby, které vznikají při sazbě práce v LaTeXu (včetně této šablony) a které
Word nedělá. Každá chyba má příznak v PDF (nebo v logu překladu) a odkaz na
pravidlo, které porušuje. Kde žádné pravidlo neexistuje, je zdrojem
`rozhodnutí repa` — snaha, aby výstup z LaTeXu vypadal jako práce z Wordu.

`zdroj` v poli Ověření tady znamená zdrojové soubory `.tex` nebo log překladu
(`.log`).

## Formální

### LTX-F01 Řádek přetéká do okraje
- Pravidlo: Žádný řádek textu, vzorce, tabulky ani URL nepřesahuje pravý okraj textu (overfull \hbox).
- Zdroj: viz DOK-F02
- Varianty: —
- Ověření: PDF + zdroj — inkoust řádku za x ≈ 525 pt; v logu „Overfull \hbox“ větší než ≈ 1 pt
- Štítky: latex, poloha, měření, zdrojový-soubor
- Poznámka: Častá příčina: dlouhá URL, dlouhé slovo bez možnosti dělení, široká tabulka nebo obrázek s `width` větší než `\textwidth`.

### LTX-F02 Roztažené mezery mezi slovy
- Pravidlo: Mezery mezi slovy v řádcích zarovnaných do bloku nejsou výrazně větší než obvykle (underfull \hbox, „řeka“ mezer).
- Zdroj: viz DOK-F05; viz DOK-F10
- Varianty: —
- Ověření: PDF + zdroj — řádek, ve kterém je průměrná mezera mezi slovy > 2× běžné; v logu „Underfull \hbox (badness 10000)“
- Štítky: latex, zarovnání, dělení-slov, měření, zdrojový-soubor

### LTX-F03 Prázdné nebo téměř prázdné stránky
- Pravidlo: V práci nejsou prázdné stránky (např. z `\cleardoublepage`) ani stránky s několika řádky textu a velkou dírou pod nimi, které nejsou koncem kapitoly.
- Zdroj: viz DOK-F06; viz DOK-F15
- Varianty: —
- Ověření: PDF — stránka bez inkoustu (kromě záhlaví a čísla); stránka uprostřed kapitoly zaplněná méně než ze ⅓
- Štítky: latex, stránkování, měření

### LTX-F04 Natažené mezery na stránce
- Pravidlo: Mezery mezi odstavci a kolem nadpisů jsou na všech stránkách stejné; LaTeX je nesmí natahovat, aby zaplnil stránku (`\flushbottom`, pružné mezery).
- Zdroj: viz DOK-F05; viz DOK-F18
- Varianty: —
- Ověření: PDF — mezera mezi odstavci na některé stránce o > 2 pt větší než typická mezera v práci
- Štítky: latex, mezery, jednotnost, měření

### LTX-F05 Plovoucí obrázky a tabulky daleko od textu
- Pravidlo: Obrázek nebo tabulka je na stejné nebo následující stránce jako text, který ho uvádí; obrázky se nehromadí na konci kapitoly ani na samostatných stránkách s plovoucími objekty.
- Zdroj: rozhodnutí repa
- Varianty: —
- Ověření: PDF — první zmínka „Obr. N“ / „Tab. N“ v textu je víc než o stránku dál od objektu; stránka jen s obrázky na konci kapitoly
- Štítky: latex, obrázek, tabulka, stránkování, text, měření
- Poznámka: Ve Wordu je obrázek přímo v toku textu, takže tahle chyba nevzniká.

### LTX-F06 Barevné nebo orámované odkazy
- Pravidlo: Odkazy (obsah, křížové odkazy, citace, URL) nemají barvu ani rámeček.
- Zdroj: viz DOK-F12
- Varianty: —
- Ověření: PDF — barevný text nebo rámečky anotací odkazů (hyperref bez `hidelinks`)
- Štítky: latex, barva, měření, zdrojový-soubor

### LTX-F07 Nevyřešené odkazy
- Pravidlo: V PDF nejsou nevyřešené odkazy „??“ ani nevyřešené citace („[?]“, tučný klíč citace).
- Zdroj: viz CIT-F01; viz OBS-F05
- Varianty: —
- Ověření: PDF + zdroj — text „??“ nebo „[?]“; v logu „undefined references“ / „Citation … undefined“
- Štítky: latex, citace, text, zdrojový-soubor

### LTX-F08 Chybějící znaky nebo náhradní písmo
- Pravidlo: Všechny znaky jsou vysázené písmem práce; nechybí žádný znak (diakritika, „“, –, …) a není nahrazený jiným písmem.
- Zdroj: viz DOK-F03; viz DOK-F04
- Varianty: —
- Ověření: PDF + zdroj — v pdffonts jen očekávaná písma; v logu „Missing character“; v textu prázdné místo nebo □
- Štítky: latex, písmo, text, zdrojový-soubor

### LTX-F09 Anglické uvozovky a spojovník místo pomlčky
- Pravidlo: Uvozovky jsou české „…“, ne ``…'' ani “…”; rozsahy a vsuvky mají pomlčku (–, v LaTeXu `--`), ne spojovník.
- Zdroj: viz DOK-F13
- Varianty: —
- Ověření: PDF — znaky “ ” ‘ ’ " v textu; „číslo-číslo“ se spojovníkem
- Štítky: latex, uvozovky, pomlčky, text

### LTX-F10 Výchozí popisky a číslování z třídy dokumentu
- Pravidlo: Titulky mají tvar „Obr. N:“ / „Tab. N:“ (ne „Obrázek 2.1:“), číslování obrázků a tabulek je průběžné (ne po kapitolách) a nadpis kapitoly nemá slovo „Kapitola“.
- Zdroj: viz OBR-F02; viz OBR-F03; viz TAB-F02; viz NA1-F03
- Varianty: —
- Ověření: PDF — text „Obrázek “, „Tabulka “, „Kapitola “ nebo číslo ve tvaru „N.M“ v titulku
- Štítky: latex, titulek, číslování, nadpis, text

### LTX-F11 Ligatury
- Pravidlo: Text nemá ligatury fi, fl, ff, ffi (Word je ve výchozím stavu nesází).
- Zdroj: rozhodnutí repa
- Varianty: —
- Ověření: PDF — v textu znaky U+FB00–U+FB04 nebo ligatury v glyfech písma
- Štítky: latex, písmo, jednotnost, text
- Poznámka: Šablona to řeší volbou `Ligatures=NoCommon`; vlastní úpravy písma ji můžou zrušit.

### LTX-F12 Jednopísmenné předložky na konci řádku
- Pravidlo: Jednopísmenné předložky a spojky nezůstávají na konci řádku; v LaTeXu to zajišťuje balíček xevlna nebo ruční `~`.
- Zdroj: viz DOK-F11
- Varianty: —
- Ověření: PDF — řádek končí slovem k/s/v/z/o/u/i/a
- Štítky: latex, pevné-mezery, text
- Poznámka: xevlna nefunguje v matematice a ve verbatim prostředích; tam je potřeba `~` napsat ručně.

### LTX-F13 Mezery ve výčtech
- Pravidlo: Výčty nemají mezery mezi položkami ani zvětšené mezery před a za seznamem (výchozí itemize/enumerate je má).
- Zdroj: viz VYC-F03
- Varianty: —
- Ověření: PDF — rozteč položek výčtu > 17 pt
- Štítky: latex, výčet, mezery, měření

## Obsahová

Zatím bez pravidel (k doplnění).
