# Zdrojové soubory práce

Každá část dokumentu má vlastní soubor. Najdi ten správný a piš – strukturu za tebe řídí `semestralni_prace.tex`.

## Co upravovat

| Soubor | Obsah |
|---|---|
| `abstrakt.tex` | Abstrakt česky, klíčová slova, překlad do angličtiny |
| `uvod.tex` | Úvod práce |
| `text.tex` | Hlavní text – teoretická část, praktická část, obrázky, tabulky, citace |
| `zaver.tex` | Závěr |
| `seznam_literatury.tex` | Seznam použité literatury |
| `prilohy.tex` | Přílohy (nemáš-li žádné, nech prázdné) |
| `podekovani.tex` | Poděkování (nepovinné) |
| `seznamy.tex` | Seznam zkratek; LOF a LOT se generují automaticky |

## Co neupravovat

| Soubor | Proč |
|---|---|
| `semestralni_prace.tex` | Řídí pořadí kapitol |
| `title_page.tex` | Titulní strana – data se berou z `conf/settings.sty` |
| `prohlaseni.tex` | Text je daný předpisem, datum se doplní automaticky |
| `obsah.tex` | Generuje se automaticky z nadpisů v textu |

## Nadpisy

```latex
\chapter{Název kapitoly}       % první úroveň (Nadpis 1)
\section{Název podkapitoly}    % druhá úroveň (Nadpis 2)
\subsection{Název oddílu}      % třetí úroveň (Nadpis 3)
```

VŠPJ vyžaduje nejvýše tři úrovně nadpisů.

## Podadresáře

- [`conf/`](conf/README.md) – nastavení šablony; vyplň zde své osobní údaje
- [`img/`](img/README.md) – sem ukládej obrázky a grafy
