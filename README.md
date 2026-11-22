# Šablona závěrečné práce – VŠPJ

LaTeXová šablona pro psaní bakalářských a jiných závěrečných prací na Vysoké škole polytechnické Jihlava. Vizuálně odpovídá oficiálnímu vzoru v `Dokumenty/Sablona.docx`.

## Jak začít

1. **Forkni** tento repozitář na svůj GitHub účet.
2. **Vyplň své údaje** v [`src/conf/settings.sty`](src/conf/README.md) – jméno, název práce, vedoucí, rok.
3. **Piš** – přehled souborů a co do každého patří najdeš v [`src/`](src/README.md).

## Sestavení PDF

**GitHub Actions (doporučeno)** – při každém `push` do větve `main` se PDF automaticky zkompiluje a uloží do `Verze/` s časovým razítkem. Nevyžaduje žádnou instalaci.

**Lokálně** – vyžaduje [Docker](https://www.docker.com/):
```bash
./build.sh        # nebo: make build
make clean        # smaže output/ a dočasné soubory
```
PDF se uloží do `output/`.

**Rychlý náhled bez Dockeru** – vyžaduje [tectonic](https://tectonic-typesetting.github.io/) a font Carlito:
```bash
make fast         # → output/prace.pdf, log v output/logs/build.log
```
Tectonic má vlastní sadu balíků, výsledek se proto může drobně lišit. Rozhodující je PDF z GitHub Actions nebo z `./build.sh`.

## Aktualizace šablony ve vlastní práci

Šablona se průběžně opravuje. Novou verzi si stáhneš do své práce přes git — funguje to u forku i u soukromé kopie (GitHub nedovolí soukromý fork veřejného repozitáře; soukromou kopii vytvoříš tak, že šablonu naklonuješ a pushneš do nového soukromého repozitáře, historie zůstane společná):
```bash
git remote add sablona https://github.com/CalaVSPJ/VSPJ_LaTeX_sablona.git   # jednou
git fetch sablona
git merge sablona/main
```
Konflikty vzniknou tam, kde šablona změnila vzorový text, který jsi už nahradil(a) svým. Pravidlo: **formát ze šablony, obsah tvůj** — v `src/conf/settings.sty` si nech své proměnné, v kapitolách, literatuře a seznamech svůj text, ale převezmi nová makra a nastavení (např. `\zkratka`, `\nadpisOddilu`). Po sloučení sestav PDF a zkontroluj ho (viz Kontrola práce).

## Kontrola práce

Hotové PDF můžeš nechat zkontrolovat podle pravidel VŠPJ skillem pro Claude Code —
návod je v [`.claude/skills/kontrola-prace/README.md`](.claude/skills/kontrola-prace/README.md).

## Struktura repozitáře

```
├── src/            ← tvůj text; každá kapitola má vlastní soubor
│   ├── conf/       ← nastavení šablony a proměnné (jméno, název práce…)
│   └── img/        ← obrázky a grafy vložené do práce
├── Dokumenty/      ← oficiální vzor VŠPJ (neupravuj)
├── .claude/skills/ ← skill Claude Code pro kontrolu práce (viz .claude/skills/kontrola-prace/README.md)
├── .claude/agents/ ← subagent, kterému skill předává kontrolu jednotlivých částí
├── docs/           ← pravidla závěrečné práce a dokumentace (viz docs/README.md)
├── Verze/          ← PDF generované při každém push
└── output/         ← PDF z lokální kompilace
```
