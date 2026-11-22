# Obrázek

Obrázky, fotografie, schémata a grafy v textu práce (graf je druh obrázku).
Obrázky v přílohách se řídí stejnými pravidly, pokud PRI neříká jinak.

## Rozpoznání

Grafický objekt (bitmapa nebo vektorová kresba) v textu, pod ním řádek začínající „Obr. N:“.

## Formální

### OBR-F01 Umístění
- Pravidlo: Obrázek je na samostatném řádku, zarovnaný na střed textové plochy.
- Zdroj: příručka 6.2; šablona pokyn v kapitole 2; Word PDF s. 13 (změřeno)
- Varianty: —
- Ověření: PDF — střed obrázku ≈ 311,6 pt (±3), vedle obrázku není text
- Štítky: obrázek, zarovnání, měření

### OBR-F02 Titulek
- Pravidlo: Titulek je pod obrázkem ve tvaru „Obr. N: popis“, Calibri 10 pt, tučně, na střed, mezera za 0 pt; na konci titulku není tečka a slova se v něm nedělí.
- Zdroj: šablona styl Titulek; příručka 3, 4.1, 6.2; šablona pokyn v kapitole 2; Word PDF s. 13
- Varianty: —
- Ověření: PDF — řádek pod obrázkem začíná „Obr. “ + číslo + „:“, výška písma 10 pt, tučně, střed ≈ 311,6 pt, nekončí tečkou
- Štítky: obrázek, titulek, písmo, zarovnání, interpunkce, měření, text
- Poznámka: Příručka připouští titulek o 1–2 pt menší než základní písmo (9–10 pt); šablona má 10 pt.

### OBR-F03 Číslování
- Pravidlo: Obrázky jsou číslované arabskými číslicemi průběžně v celé práci (1, 2, 3…), ne po kapitolách; grafy a schémata se číslují jako obrázky („Obr.“).
- Zdroj: šablona styl Titulek (pole SEQ Obr.); příručka 6.2
- Varianty: —
- Ověření: PDF — čísla titulků „Obr. N“ jdou v pořadí 1, 2, 3… bez mezer a opakování, žádné „Obr. 2.1“ ani „Graf 1“
- Štítky: obrázek, titulek, číslování, text

### OBR-F04 Zdroj
- Pravidlo: Pod titulkem je řádek se zdrojem, Calibri 10 pt, kurzívou, na střed, mezera za 6 pt.
- Zdroj: šablona styl Zdroj; příručka 3, 6.2; šablona pokyn v kapitole 2; Word PDF s. 13
- Varianty:
  - a) „zdroj: …“ s malým písmenem — příručka 6.2 (Obr. 1, Obr. 2)
  - b) „Zdroj: …“ s velkým písmenem — šablona pokyn v kapitole 2; Word PDF s. 13
- Ověření: PDF — řádek hned pod titulkem začíná „Zdroj:“ nebo „zdroj:“, 10 pt, kurzíva, na střed
- Štítky: obrázek, zdroj, písmo, zarovnání, měření, text

### OBR-F05 Mezery
- Pravidlo: Titulek je ≈ 19,5 pt pod spodní hranou obrázku (inkoust), zdroj hned pod titulkem (rozteč ≈ 14 pt), za zdrojem běžná mezera 6 pt před dalším odstavcem.
- Zdroj: Word PDF s. 13 (změřeno); šablona styl Titulek; šablona styl Zdroj
- Varianty: —
- Ověření: PDF — spodní hrana obrázku → horní hrana titulku ≈ 19,5 pt (±4), horní hrany titulku a zdroje ≈ 14 pt (±1,5); stejné u všech obrázků (viz DOK-F18)
- Štítky: obrázek, titulek, zdroj, mezery, měření

### OBR-F06 Velikost a poměr stran
- Pravidlo: Obrázek nepřesahuje šířku textu (425,15 pt); pokud to jde, využije celou šířku. Poměr výšky a šířky musí být zachován (obrázek není zdeformovaný).
- Zdroj: příručka 6.2
- Varianty: —
- Ověření: PDF — šířka obrázku ≤ 425,15 pt; zdroj — u `\includegraphics` nejsou zároveň `width` a `height` bez `keepaspectratio`
- Štítky: obrázek, měření, zdrojový-soubor

### OBR-F07 Rámeček a vzhled
- Pravidlo: Obrázky nemají rámeček, ledaže je k tomu vážný důvod; pak jsou orámované všechny stejně. Grafy a schémata jsou jednoduché, bez ozdob, 3D efektů a stínů; všechny grafy mají stejný vzhled.
- Zdroj: příručka 6.2
- Varianty: —
- Ověření: PDF — rámeček kolem obrázku (souvislá čára po obvodu) jen pokud ho mají všechny obrázky; vzhled grafů posoudit vizuálně
- Štítky: obrázek, jednotnost, posouzení

## Obsahová

### OBR-O01 Popis v titulku
- Pravidlo: Titulek krátce popisuje, co je na obrázku.
- Zdroj: příručka 6.2; šablona pokyn v kapitole 2
- Varianty: —
- Ověření: PDF — titulek obsahuje popis (není jen „Obr. N:“ nebo „Obrázek“)
- Štítky: obrázek, titulek, obsah-textu, posouzení

### OBR-O02 Zdroj uveden vždy
- Pravidlo: Zdroj se uvádí u každého obrázku, i vlastního: „vlastní zpracování“, „vlastní fotografie (rok pořízení)“ apod. (rok zpracování se jinak neuvádí). Převzatý obrázek má odkaz v harvardském stylu (viz CIT-F01) a citaci v seznamu literatury.
- Zdroj: příručka 6.2; šablona pokyn v kapitole 2
- Varianty: —
- Ověření: PDF — každý titulek „Obr.“ má pod sebou řádek se zdrojem; převzatý zdroj odpovídá položce seznamu literatury
- Štítky: obrázek, zdroj, citace, text

### OBR-O03 Vhodný typ grafu
- Pravidlo: Typ grafu odpovídá zobrazovaným veličinám; nevhodně zvolený typ grafu je hrubá chyba.
- Zdroj: příručka 6.2
- Varianty: —
- Ověření: PDF — posouzení obsahu grafu
- Štítky: obrázek, obsah-textu, posouzení
