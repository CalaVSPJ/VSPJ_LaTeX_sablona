# Nastavení šablony

Soubor `settings.sty` obsahuje veškeré formátování šablony – fonty, okraje, velikosti nadpisů a další. **Neupravuj ho**, pokud přesně nevíš, co děláš; změna může narušit shodu s oficiálním vzorem VŠPJ.

## Co upravit

Jedinou částí, do které zasahuješ, jsou proměnné na začátku souboru:

```latex
\newcommand{\varProgram}{Studijní program}            % název studijního programu
\newcommand{\varThesisType}{Bakalářská práce}         % typ práce
\newcommand{\varThesisName}{Název práce}              % celý název tvé práce
\newcommand{\varAuthor}{Jméno Příjmení}               % tvoje jméno a příjmení
\newcommand{\varTutor}{titul Jméno Příjmení, titul}   % vedoucí práce včetně titulů
\newcommand{\varCity}{Jihlava}                        % místo odevzdání
\newcommand{\varYear}{2026}                           % rok odevzdání
```

Tyto hodnoty se automaticky propíší na titulní stranu, do prohlášení a dalších částí dokumentu – vyplníš je jednou a v celé práci se aktualizují samy.
