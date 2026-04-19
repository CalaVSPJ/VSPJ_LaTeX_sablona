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
./build.sh
```
PDF se uloží do `output/`.

## Struktura repozitáře

```
├── src/            ← tvůj text; každá kapitola má vlastní soubor
│   ├── conf/       ← nastavení šablony a proměnné (jméno, název práce…)
│   └── img/        ← obrázky a grafy vložené do práce
├── Dokumenty/      ← oficiální vzor VŠPJ (neupravuj)
├── Verze/          ← PDF generované při každém push
└── output/         ← PDF z lokální kompilace
```
