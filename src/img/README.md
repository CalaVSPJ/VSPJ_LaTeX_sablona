# Obrázky a grafy

Sem ukládej všechny obrázky a grafy, které chceš vložit do práce.

## Podporované formáty

| Formát | Kdy použít |
|---|---|
| PDF | vektorová grafika, grafy z Excelu/R/Pythonu – nejlepší kvalita tisku |
| PNG | snímky obrazovky, diagramy s průhledností |
| JPG | fotografie |

## Vložení do dokumentu

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.6\textwidth]{src/img/nazev_souboru.pdf}
    \caption{Popis obrázku}
    \small\textit{Zdroj: Příjmení (rok, s. X)}
\end{figure}
```

Číslo obrázku se doplní automaticky. Odkaz na obrázek v textu: `(viz Obr.~\ref{fig:label})` – k tomu přidej `\label{fig:label}` za `\caption`.
