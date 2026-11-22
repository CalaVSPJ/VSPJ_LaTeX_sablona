# Pomocné dokumenty

Tyto dokumenty slouží jako pomocníci při psaní seminárních prací na VŠPJ.

## Šablona

Z důvodu přímého zobrazení na githubu, a jiných zařízeních, byla původní šablona ve formátů `.docx` překonvertována na formát `.pdf`.

Aktuální `Sablona.docx` je verze **„šablona ZP 2023“** (naposledy upravena 28. 4. 2023). Od předchozí verze z 1. 7. 2022 se obsahem ani styly neliší.
Rok na titulní straně je pole `TIME \@ "yyyy"` — Word ho při otevření přepíše na aktuální rok, o stáří šablony tedy nic neříká.

Číslování stránek se v šabloně řídí příručkou *Jak psát práce na VŠPJ* (kap. 12–13: číslo od Obsahu, přílohy bez čísla); DOCX vzor má Obsah a Seznamy bez čísla.

Původní Sablona.docx (verze 2022) byla stáhnuta [zde](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiW29fFzvmTAxXe8LsIHUn4OZ4QFnoECA4QAQ&url=https%3A%2F%2Fkcr.vspj.cz%2Fcs%2Fsoubor%2Fstahnout%2Fb9e7c558-9270-4842-b13a-79274952bbf0&usg=AOvVaw3om2A0JcYnforHAd5Khiho&opi=89978449)

`Sablona.pdf` je export z **Word Online** (Soubor → Stáhnout jako PDF), takže obsahuje skutečná písma Calibri a Calibri Light.

Převod přes LibreOffice (`libreoffice --headless --convert-to pdf Sablona.docx`) se nedoporučuje: Calibri sice nahradí metricky shodným Carlito, ale pro Calibri Light (nadpisy) náhradu nemá a použije patkové písmo — nadpisy pak vypadají jinak a titulní strana se rozteče na dvě stránky.

## ❗Důležité❗

Bohužel nejsem si vědom systematického přístupu při sdílení těchto a podobných dokumentů. Bylo by vhodné, kdyby existoval endpoint na VŠPJ, ze kterého by vždy, například příkazem `curl` bylo možno stáhnout poslední verzi šablony, případně jiných relevantních dokumentů.

V případě budoucí existence je vhodné přidat do `.github/workflows` automatizaci, která bude tyto soubory do budoucna obstarávat a držet aktuální.