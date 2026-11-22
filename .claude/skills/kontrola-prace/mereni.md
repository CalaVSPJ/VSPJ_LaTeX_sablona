# Jak číst fakta z `vytahni.py`

Platí pro hlavní kontrolu i pro subagenta `kontrola-casti`.

- Hodnoty v pravidlech jsou měřené z **pásů inkoustu** (`pasy`, `prvni_pas`,
  `posledni_pas`) — horní hrana inkoustu řádku. Polohy porovnávej s nimi;
  `prvni_radek_top` a `bbox` řádků jsou rámečky textu (o ≈ 1 pt jiné).
  Písmo a velikost porovnávej s `useky`.
- U řádku s diakritikou nad verzálkami může být první pás jen čárky a háčky;
  hodnoty v pravidlech byly měřené stejně — porovnávej první pás tak, jak je.
- **Velikost písma:** LaTeX měří v TeX bodech (1/72,27 palce), takže 18 pt
  vyjde jako 17,9 a 14 pt jako 13,9. Rozdíl ≤ 0,15 pt není chyba.
- **Tučnost:** nadpisy jsou tučné dopočtením (FakeBold v LaTeXu, syntetická
  tučnost ve Wordu) — název písma není „Bold“. Tučný úsek poznáš podle
  `tucne == true` **nebo** `vyplnovani == "fill+stroke"`.
- Písmo Carlito je přijatelná náhrada Calibri (DOK-F03, DOK-F04).
- Vektorové obrázky (PDF, kresby) nejsou v `obrazky`, ale v `cary`.
- `strana` je fyzická strana PDF; tištěné číslo je v `cislo_stranky`.
- Strana s `rotace` ≠ 0 je na šířku (nepopsaný prvek) — polohová pravidla na ní
  nehodnoť. Okraje ve skriptu platí pro A4; jiný rozměr v `rozmery` uveď jako
  poznámku a polohy na takové straně nehodnoť.
- `mimo_okraje` uvnitř výpisu kódu (např. čísla řádků) je nepopsaný prvek,
  ne LTX-F01.

## Závažnost

- **chyba** — pravidlo bez variant porušené, nebo stav neodpovídá žádné variantě;
- **upozornění** — pravidlo, jehož jediným zdrojem je `seminář …`, pravidlo
  označené jako doporučení, každý výsledek „posouzení“;
- **poznámka** — míchání variant, nepopsané prvky, rozsah práce, přeskočené
  kontroly (chybí log, záložní režim, jiný rozměr strany).
