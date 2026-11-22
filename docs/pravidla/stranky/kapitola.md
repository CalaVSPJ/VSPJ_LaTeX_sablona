# Kapitola

Běžná číslovaná kapitola textu práce (teoretická, praktická část…).

## Rozpoznání

Každá stránka, která začíná nadpisem 1. úrovně s číslem („1 …“, „2 …“), až do další kapitoly nebo „Závěr“.

## Formální

### KAP-F01 Začátek kapitoly
- Pravidlo: Kapitola začíná na nové stránce číslovaným nadpisem 1. úrovně (viz NA1-F03, DOK-F15) a hned za nadpisem je odstavec textu (viz NA1-O02).
- Zdroj: šablona styl Nadpis 1; šablona pokyn v Úvodu; příručka 3
- Varianty: —
- Ověření: PDF — nadpis „N Název“ jako první řádek stránky, pod ním řádek základního textu
- Štítky: nadpis, stránkování, struktura, měření

### KAP-F02 Číslování návazné
- Pravidlo: Kapitoly, podkapitoly a oddíly jsou číslované vzestupně bez vynechání (1, 2, 3; 1.1, 1.2; 1.1.1, 1.1.2); nejvýš tři úrovně (viz DOK-F16).
- Zdroj: příručka 5.1; šablona styl Nadpis 1
- Varianty: —
- Ověření: PDF — posloupnost čísel nadpisů nemá mezery ani opakování a podkapitoly patří k číslu nadřazené kapitoly
- Štítky: nadpis, číslování, text

## Obsahová

Účel: Kapitoly tvoří jádro práce — teoretické východisko a vlastní řešení.
Jejich skladba se řídí typem práce (implementační, návrhová, srovnávací,
kombinovaná); osnovy níže jsou doporučení Katedry technických studií
a vedoucí práce může mít upřesňující požadavky.

### KAP-O02 Skladba kapitol
- Pravidlo: Názvy a skladba kapitol jsou doporučené a mohou se lišit podle tématu a katedry (viz DOK-O03).
- Zdroj: šablona pokyn v Úvodu
- Varianty: —
- Ověření: PDF — nekontroluje se (jen informace pro kontrolu: neodlišné názvy kapitol nejsou chyba)
- Štítky: struktura, posouzení

### KAP-O03 Teoretická část
- Pravidlo: První kapitola (teoretická část) popisuje současný stav problematiky a vymezuje pojmy, se kterými práce pracuje.
- Zdroj: seminář Rešerše
- Varianty: —
- Ověření: PDF — posouzení: kapitola 1 obsahuje definice pojmů a přehled stavu oboru s odkazy na zdroje (viz CIT-F01)
- Štítky: obsah-textu, struktura, posouzení

### KAP-O04 Rešerše a reakce na ni
- Pravidlo: Výsledky rešerše (zhuštěný souhrn informací o tom, kde, kým a jak byl předmět zkoumán) jsou typicky v podkapitole 1.1 a vlastní část práce na ně reaguje.
- Zdroj: seminář Rešerše
- Varianty: —
- Ověření: PDF — posouzení: v teoretické části je přehled existujících řešení / výzkumů se zdroji; praktická část se k němu vztahuje (navazuje, srovnává, vymezuje se)
- Štítky: obsah-textu, citace, posouzení

### KAP-O05 Určení typu práce
- Pravidlo: Typ práce (implementační, návrhová, srovnávací / rešeršní, kombinovaná) se určí ze zadání nebo z cíle v úvodu; u kombinované práce musí být zřejmé, která část je stěžejní. Podle typu se použije osnova KAP-O06 až KAP-O08.
- Zdroj: seminář Typy BP
- Varianty: —
- Ověření: PDF — posouzení zadání (s. 2) a cíle v úvodu (viz UVO-O01). U kombinované práce se kontroluje osnova stěžejní části a u vedlejší části jen její přítomnost (např. rešeršní část jako východisko implementace nemusí mít srovnávací metodiku). Když typ nebo stěžejní část nejde určit, kontrolují se jen společné prvky (KAP-O09, KAP-O03) a kontrola upozorní, že typ práce nezná
- Štítky: obsah-textu, struktura, posouzení
- Poznámka: Kombinace má být podle semináře uvedena už v textu zadání (např. „rešeršně-implementační“).

### KAP-O06 Osnova implementační práce
- Pravidlo: Implementační práce (výsledkem je hotový použitelný produkt — HW nebo SW) obsahuje: popis řešeného problému a požadavků na systém; rešerši existujících implementací, jsou-li známy; analýzu a návrh včetně diskuse alternativ a zdůvodnění volby implementačního prostředí (jazyk, knihovny, nástroje, technologie); popis implementace zaměřený na nestandardní části řešení; jednoduchý návod nejvýše na 2 strany s podmínkami instalace a spuštění; výsledky testů funkčnosti a výkonnosti; srovnání s existujícími řešeními, jsou-li známa. Uživatelská a programátorská část se nemíchají.
- Zdroj: seminář Typy BP; seminář Chyby
- Varianty: —
- Ověření: PDF — posouzení: kapitoly nebo podkapitoly odpovídající prvkům osnovy; návod ≤ 2 strany; kapitola s testy; chybějící prvek → upozornění
- Štítky: obsah-textu, struktura, posouzení

### KAP-O07 Osnova návrhové práce
- Pravidlo: Návrhová práce (těžištěm je analýza netriviálního problému a návrh řešení) obsahuje: přesné vymezení cílů a požadavků na navrhovaný systém; analýzu a diskusi variant návrhu; popis výsledného návrhu ve vhodném formálním aparátu (např. UML) se zdůvodněním voleb; ověření funkčnosti a správnosti návrhu (formální verifikace, matematický nebo simulační model); srovnání s podobnými návrhy, existují-li. Implementace prototypu není nutná.
- Zdroj: seminář Typy BP
- Varianty: —
- Ověření: PDF — posouzení: je přítomna analýza variant, zdůvodněný návrh a jeho ověření; návrh bez jakéhokoli ověření → upozornění
- Štítky: obsah-textu, struktura, posouzení

### KAP-O08 Osnova srovnávací (rešeršní) práce
- Pravidlo: Srovnávací práce obsahuje: podrobný popis srovnávaných systémů nebo řešení; specifikaci kritérií srovnání; popis nebo návrh srovnávací metodiky (metriky, testy, zkušební úlohy); podrobný popis výsledků srovnání; zobecnění výsledků (nové souvislosti, rozdíly, podobnosti).
- Zdroj: seminář Typy BP
- Varianty: —
- Ověření: PDF — posouzení: jsou výslovně uvedena kritéria a metodika srovnání a závěry jsou zobecněné, ne jen výčet vlastností
- Štítky: obsah-textu, struktura, posouzení

### KAP-O09 Struktura práce ve vztahu k cílům
- Pravidlo: Práce popisuje svou strukturu ve vztahu k vytyčeným cílům — čtenář ví, ve které kapitole se plní který cíl. Kapitoly na sebe logicky navazují (soulad obsahu se zadáním viz DOK-O06).
- Zdroj: seminář Typy BP; seminář Chyby
- Varianty: —
- Ověření: PDF — posouzení: v úvodu nebo na začátku kapitol je popis struktury práce; každý cíl z úvodu má kapitolu, která ho řeší
- Štítky: obsah-textu, struktura, posouzení
