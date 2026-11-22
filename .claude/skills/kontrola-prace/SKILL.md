---
name: kontrola-prace
description: Zkontroluje PDF bakalářské nebo diplomové práce vysázené v této LaTeX šabloně VŠPJ podle pravidel v docs/pravidla (formát, struktura, úvod, závěr, abstrakt, citace, odborný styl) a zapíše hlášení s ID pravidel do output/. Použij, když uživatel chce zkontrolovat práci nebo její část („zkontroluj práci“, „zkontroluj úvod / citace / titulní stranu / formát“, „kontrola práce“).
---

# Kontrola závěrečné práce

Kontroluješ PDF práce podle pravidel v `docs/pravidla/`. Pravidla jsou jediný
zdroj pravdy: hodnoť **jen** podle nich a u každého nálezu uveď ID pravidla.
Celou práci si sám zmapuješ a zkontroluješ věci přes celou práci; části
rozdělíš mezi subagenty `kontrola-casti` a jejich nálezy sloučíš do hlášení.

## Zásady

- **Nic neměň.** Během kontroly neupravuj `.tex` ani jiné soubory práce. Skill
  jen upozorňuje (stupeň 2 — Asistence podle MP č. 8/2026). Pokud o to uživatel
  po kontrole výslovně požádá, smíš opravit formální a sazební věci (makra,
  mezery, nastavení); obsah práce (věty, argumentaci, závěry) nepiš.
- **Bez souhlasu nic nespouštěj navíc:** nesestavuj PDF, neinstaluj balíčky —
  nabídni příkaz a počkej. Zapisuj jen do `output/`.
- **Čísla neodhaduj.** Formální pravidla posuzuj podle hodnot z `vytahni.py`
  a uveď změřenou i očekávanou hodnotu. Odhad (záložní režim, posouzení)
  takto označ.
- **Varianty:** pravidlo s Variantami je splněné, když práce odpovídá
  kterékoli z nich; zjisti, kterou práce používá, a drž ji v celé práci.
- **Šetři kontext:** podrobná fakta stran načítají subagenti; ty pracuješ se
  souhrnem. Sám `--strany` / `--text` spouštěj jen na zjištění variant (jedna
  strana literatury, jedna strana textu) a na strany s `mimo_okraje` > 0;
  písma, polohy nadpisů a text kapitol nech subagentům.

## Postup

Skripty spouštěj z kořene repa vždy celou cestou
(`python3 .claude/skills/kontrola-prace/vytahni.py …`). Jako `python3` použij
`.venv/bin/python` (Windows `.venv/Scripts/python`), pokud v repu existuje
`.venv/`. Jak číst fakta a určit závažnost: přečti
`.claude/skills/kontrola-prace/mereni.md`.

1. **PDF.** Použij cestu od uživatele. Jinak vyber nejnovější podle data:
   lokální `output/prace_RRRR-MM-DD_HH-MM.pdf` (z `./build.sh`), `output/prace.pdf`
   a `Verze/prace_DD-MM-RRRR_HHMM.pdf` (z GitHub Actions) — datum ber z názvu
   souboru, ne z času změny. Uživateli řekni, které PDF jsi vybral. Je-li
   novější commit nebo soubor v `src/` než datum PDF, upozorni a nabídni
   `./build.sh`. Log překladu: `output/logs/build.log` (když chybí, pravidla
   s logem přeskoč s poznámkou).
2. **Závislosti.** `python3 -c "import pymupdf"`. Když chybí, nabídni
   instalaci (`python3 -m venv .venv` a `.venv/bin/pip install pymupdf`). Nejde-li
   to, pokračuj v **záložním režimu**: PDF čti jako obrázky a text a všechny
   měřené hodnoty označ jako odhad (bez subagentů).
3. **Mapa.** `python3 .claude/skills/kontrola-prace/vytahni.py PDF --souhrn`
   → přiřaď fyzické strany k typům podle sekcí `## Rozpoznání` v pravidlech:
   1 titulní, 2 zadání, 3 abstrakt, 4 prohlášení, 5 poděkování (nepovinné —
   jinak 5 obsah), pak obsah a dál podle nadpisů 1. úrovně (`prvni_radek`)
   a záložek PDF (`zalozky`). Strany s obrázky nebo tabulkami poznáš podle
   `obrazku` a `car` > 0.
4. **Varianty.** Zjisti a zapiš použité varianty: číslování stran (DOK-F09 —
   od Obsahu / od Úvodu), citační systém (CIT-F01 a/b/c; určuje i CIT-F03–F05,
   BIB-F03, BIB-O01; zjisti z textu seznamu literatury a jedné strany textu),
   dělení slov (DOK-F10), typ práce (KAP-O05). Pravidla načti
   `python3 .claude/skills/kontrola-prace/pravidla.py --id …`.
5. **Celá práce** (sám, ze souhrnu a logu): `pravidla.py --soubor dokument.md`
   a `--soubor latex-chyby.md`. Zkontroluj papír a okraje (DOK-F01, DOK-F02 —
   `rozmery`, `mimo_okraje` > 0 → podrobně jen ty strany), záhlaví a čísla
   stran (DOK-F08, DOK-F09 — `zahlavi`, `cislo_stranky`, `prvni_pas`,
   `posledni_pas`), kapitolu na nové stránce a pořadí částí (DOK-F15, DOK-F17),
   prázdné strany (`prazdna`), nevyřešené odkazy (`otazniky`), rozsah práce
   (DOK-F20 — součet `slov` a `znaku` stran od Úvodu po Závěr, normostrana =
   1 800 znaků) a pravidla z `latex-chyby.md`, která se ověřují z logu.
6. **Části — subagenti.** Pro každou skupinu z tabulky níže, která v práci je,
   spusť subagenta `kontrola-casti` (nástroj Agent, `subagent_type:
   "kontrola-casti"`); všechny **v jedné zprávě**, ať běží souběžně. Kapitoly
   rozděl po celých kapitolách 1. úrovně tak, aby skupina měla nejvýš
   ≈ 15 stran. Každému dej zadání:
   ```
   PDF: <cesta>
   Python: <cesta k pythonu>
   Skupina: <název>; strany: <fyzické strany> (<typ každé strany>)
   Soubory pravidel: <soubory ze skupiny>, dokument.md, latex-chyby.md
   Varianty: <zjištěné varianty s ID>
   Režim: <celá práce / jen formální (F) / jen obsahová (O)>
   Mapa práce: <typ → strany> (jen pro orientaci)
   ```
   Agent vrátí řádky `NÁLEZ`, `POZOROVÁNÍ`, `NEPOPSANÉ`, `PŘESKOČENO`,
   `BEZ NÁLEZU`. Když agent selže nebo nic nevrátí, zkontroluj jeho skupinu
   sám podle `.claude/agents/kontrola-casti.md` a uveď to v poznámkách.
7. **Sloučení.** Nálezy se stejným ID a stranou slouč. Porovnej `POZOROVÁNÍ`
   napříč skupinami (jednotnost — DOK-F18, DOK-O07, citační systém CIT-F01):
   liší-li se, ohlas to podle pravidla. Nepopsané prvky (seznam
   v `docs/pravidla/README.md`) uveď s tím, že pro ně pravidlo není.
8. **Hlášení** zapiš do `output/kontrola_<RRRR-MM-DD_HHMM>.md` a v konverzaci
   shrň počty a nejdůležitější nálezy.

### Skupiny pro subagenty

| Skupina | Strany | Soubory pravidel (`--soubor`) |
|---|---|---|
| úvodní strany | titulní až poděkování | `stranky/titulni-strana.md`, `stranky/zadani.md`, `stranky/abstrakt.md`, `stranky/prohlaseni.md`, `stranky/podekovani.md` |
| obsah a seznamy | obsah, seznamy obrázků, tabulek, zkratek | `stranky/obsah.md`, `stranky/seznam-obrazku.md`, `stranky/seznam-tabulek.md`, `stranky/seznam-zkratek.md` |
| úvod a závěr | Úvod a Závěr (spolu — závěr se porovnává s cíli úvodu) | `stranky/uvod.md`, `stranky/zaver.md` |
| kapitoly 1…n | strany kapitol, po ≈ 15 stranách | `stranky/kapitola.md`, `prvky/nadpis-1.md`, `prvky/nadpis-2.md`, `prvky/nadpis-3.md`, `prvky/vycet-seznam.md`, `prvky/poznamka-pod-carou.md` |
| literatura a citace | seznam literatury, přílohy a text Úvod–Závěr (jen `--text`, kvůli citacím) | `stranky/seznam-literatury.md`, `prvky/polozka-literatury.md`, `prvky/odkaz-v-textu.md`, `stranky/prilohy.md` |
| obrázky, tabulky, rovnice | strany s `obrazku` nebo `car` > 0 a strany s rovnicemi | `prvky/obrazek.md`, `prvky/tabulka.md`, `prvky/rovnice.md` |

U prohlášení (PRO-O01) připiš do zadání: zkontroluj i tvary typu práce ve
větách (bakalářská / bakalářskou / bakalářské práce) — v LaTeXu se typ práce
vkládá makrem.

### Režimy

- **Celá práce** (výchozí) — kroky 1–8.
- **Jedna část** („úvod“, „citace“, „titulní strana“…) — kroky 1–4, pak jen
  subagent odpovídající skupiny (a z kroku 5 jen pravidla té části); hlášení.
- **Jen formální / jen obsahová** — jako celá práce, režim předej subagentům
  (ID s `F` / s `O`).
- **Bez subagentů** (uživatel o to požádá, nebo nástroj Agent není k dispozici)
  — skupiny projdi sám jednu po druhé podle `.claude/agents/kontrola-casti.md`;
  podrobná fakta načítej jen pro právě kontrolovanou skupinu.

## Hlášení

```markdown
# Kontrola práce — <název práce>, <datum a čas>
PDF: <cesta> (<N> stran) · režim: <celá práce / část> · varianty: <např. číslování od Obsahu (DOK-F09 a), citace harvard (CIT-F01 a)>

## Souhrn
<X> chyb · <Y> upozornění · <Z> poznámek · rozsah: Úvod–Závěr <S> stran, <W> slov, <N> normostran

## Chyby
- **<ID>** s. <strana> — <co je špatně>: změřeno <hodnota>, očekáváno <hodnota / citace pravidla>.

## Upozornění
- **<ID>** (<doporučení semináře / posouzení>) s. <strana> — <popis>.

## Poznámky a nepopsané prvky
- …

## Zkontrolováno bez nálezu
<seznam ID>
```
