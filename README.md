# VŠPJ LaTeX Šablona

Tento repozitář obsahuje LaTeXovou šablonu pro psaní seminárních, bakalářských a jiných prací na Vysoké škole polytechnické Jihlava (VŠPJ). Šablona je navržena tak, aby co nejtěsněji odpovídala oficiálnímu vzoru (`Dokumenty/Sablona.pdf`).

## Vlastnosti
- **Soulad se vzorem:** Struktura a formátování odpovídají oficiálním požadavkům VŠPJ.
- **Automatizace:** Integrované GitHub Actions pro automatickou kompilaci do PDF při každém commitu.
- **Snadná lokalizace:** Možnost lokální kompilace pomocí Dockeru bez nutnosti instalace kompletního LaTeXového prostředí.
- **Pseudonymizace:** Vzorový obsah je zbaven konkrétních osobních údajů a nahrazen zástupnými symboly.

## Struktura projektu
- `src/`: Zdrojové soubory LaTeXu.
  - `conf/settings.sty`: Hlavní nastavení (fonty, balíčky, proměnné).
  - `semestralni_prace.tex`: Hlavní soubor projektu.
- `Dokumenty/`: Oficiální šablony a pokyny.
- `Verze/`: Adresář pro vygenerované verze PDF (automaticky plněno GitHub Actions).

## Jak začít

1. **Konfigurace:**
   V souboru `src/conf/settings.sty` upravte proměnné pro vaši práci:
   ```latex
   \newcommand{\varProgram}{Studijní program}
   \newcommand{\varThesisName}{NÁZEV PRÁCE}
   \newcommand{\varAuthor}{Jméno Příjmení}
   \newcommand{\varTutor}{titul Jméno Příjmení, titul}
   ```

2. **Psaní textu:**
   Jednotlivé kapitoly jsou rozděleny do samostatných souborů v `src/` (např. `uvod.tex`, `text.tex`, `zaver.tex`).

## Kompilace

### Lokální kompilace (Docker)
Pro kompilaci bez instalace LaTeXu lokálně můžete využít přiložený `Makefile` (vyžaduje nainstalovaný Docker):
```bash
make build
```
Výsledné PDF naleznete v adresáři `output/`.

### Automatická kompilace (GitHub Actions)
Při každém `push` do větve `main` (změny v adresáři `src/`) se automaticky spustí workflow, které:
1. Zkompiluje dokument.
2. Uloží výsledné PDF do adresáře `Verze/` s časovým razítkem.
3. Commitne změny zpět do repozitáře.

## Požadavky pro lokální běh
- Docker
- Make (volitelně, lze spustit příkazy z Makefile přímo)
