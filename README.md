# Šablona závěrečné práce – VŠPJ

LaTeXová šablona pro psaní bakalářských a jiných závěrečných prací na Vysoké škole polytechnické Jihlava. Vizuálně odpovídá oficiálnímu vzoru v `Dokumenty/Sablona.docx`.

---

## Jak začít

### 1. Získej šablonu

Forkni tento repozitář na svůj GitHub účet (tlačítko **Fork** vpravo nahoře). Tím získáš vlastní kopii, do které můžeš psát.

### 2. Vyplň své údaje

Otevři soubor `src/conf/settings.sty` a uprav proměnné na začátku souboru:

```latex
\newcommand{\varProgram}{Aplikovaná informatika}
\newcommand{\varThesisType}{Bakalářská práce}
\newcommand{\varThesisName}{Název mé práce}
\newcommand{\varAuthor}{Jan Novák}
\newcommand{\varTutor}{doc. Ing. Jana Veselá, Ph.D.}
\newcommand{\varYear}{2026}
```

Tyto hodnoty se automaticky propíší na titulní stranu a do dalších částí dokumentu.

### 3. Piš svoji práci

Obsah práce patří do souborů v adresáři `src/` – každá kapitola má svůj soubor. Podrobný přehled viz [`src/README.md`](src/README.md).

---

## Sestavení PDF

### Přes GitHub Actions (doporučeno, bez instalace čehokoli)

Při každém `push` do větve `main` se PDF automaticky zkompiluje a uloží do adresáře `Verze/` s časovým razítkem. Stačí uložit změny, commitnout a pushnout – PDF najdeš přímo v repozitáři.

> Workflow se spustí pouze při změnách v adresáři `src/`.

Výsledné PDF je dostupné dvěma způsoby:
- přímo v adresáři `Verze/` v repozitáři
- v záložce **Actions** → poslední běh → artefakty

### Lokálně pomocí Dockeru

Vyžaduje nainstalovaný [Docker](https://www.docker.com/).

```bash
./build.sh
```

PDF se uloží do adresáře `output/`.

---

## Struktura repozitáře

```
├── src/                  ← sem patří tvůj text
│   ├── conf/             ← nastavení šablony (upravuj jen proměnné)
│   ├── img/              ← obrázky a grafy
│   └── *.tex             ← kapitoly práce
├── Dokumenty/            ← oficiální vzor VŠPJ (neupravuj)
├── Verze/                ← automaticky generované PDF s časovým razítkem
└── output/               ← výstup lokální kompilace
```

Podrobnější popis souborů v `src/` najdeš v [`src/README.md`](src/README.md).
