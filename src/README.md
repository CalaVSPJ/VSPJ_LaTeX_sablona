# Zdrojové soubory práce

Tento adresář obsahuje vše, co tvoří tvoji práci. Každá část dokumentu má vlastní soubor – stačí najít ten správný a psát.

## Přehled souborů

| Soubor | Co v něm upravuješ |
|---|---|
| `abstrakt.tex` | Abstrakt česky, klíčová slova, překlad do angličtiny |
| `uvod.tex` | Úvod práce |
| `text.tex` | Hlavní text – teoretická a praktická část, obrázky, tabulky, citace |
| `zaver.tex` | Závěr |
| `seznam_literatury.tex` | Seznam použité literatury |
| `prilohy.tex` | Přílohy (pokud je nemáš, nech prázdné) |
| `podekovani.tex` | Poděkování (nepovinné, klidně vyprázdni) |
| `seznamy.tex` | Zkratky; seznam obrázků a tabulek se generuje automaticky |

## Co neupravovat

| Soubor | Proč |
|---|---|
| `semestralni_prace.tex` | Hlavní soubor – určuje pořadí kapitol, neměň |
| `title_page.tex` | Titulní strana – data se berou z `conf/settings.sty` |
| `prohlaseni.tex` | Prohlášení – text je daný, datum se doplní automaticky |
| `obsah.tex` | Obsah – generuje se automaticky z nadpisů v textu |

## Obrázky a grafy

Ukládej je do adresáře `img/`. Do dokumentu je vložíš příkazem:

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.6\textwidth]{src/img/nazev_souboru.pdf}
    \caption{Popis obrázku}
    \small\textit{Zdroj: ...}
\end{figure}
```

Podporované formáty: PDF, PNG, JPG. Pro nejlepší kvalitu tisku doporučujeme PDF nebo PNG.

## Nadpisy a struktura

```latex
\chapter{Název kapitoly}       % první úroveň (Nadpis 1)
\section{Název podkapitoly}    % druhá úroveň (Nadpis 2)
\subsection{Název oddílu}      % třetí úroveň (Nadpis 3)
```

Víc než tři úrovně nadpisů šablona nepodporuje (a VŠPJ je ani nevyžaduje).
