# Pomocné dokumenty

Tyto dokumenty slouží jako pomocníci při psaní seminárních prací na VŠPJ.

## Šablona

Z důvodu přímého zobrazení na githubu, a jiných zařízeních, byla původní šablona ve formátů `.docx` překonvertována na formát `.pdf`.

Původní Sablona.docx byla stáhnuta [zde](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiW29fFzvmTAxXe8LsIHUn4OZ4QFnoECA4QAQ&url=https%3A%2F%2Fkcr.vspj.cz%2Fcs%2Fsoubor%2Fstahnout%2Fb9e7c558-9270-4842-b13a-79274952bbf0&usg=AOvVaw3om2A0JcYnforHAd5Khiho&opi=89978449)

Následně byla konvertována pomocí příkazu
```
libreoffice --headless --convert-to pdf Sablona.docx
```
alternativně (Nemusí zachovat formátování správně)
```
pandoc Sablona.docx -o Sablona.pdf
```

## ❗Důležité❗

Bohužel nejsem si vědom systematického přístupu při sdílení těchto a podobných dokumentů. Bylo by vhodné, kdyby existoval endpoint na VŠPJ, ze kterého by vždy, například příkazem `curl` bylo možno stáhnout poslední verzi šablony, případně jiných relevantních dokumentů.

V případě budoucí existence je vhodné přidat do `.github/workflows` automatizaci, která bude tyto soubory do budoucna obstarávat a držet aktuální.