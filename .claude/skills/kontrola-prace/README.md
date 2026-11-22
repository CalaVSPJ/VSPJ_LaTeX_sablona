# Kontrola práce (skill pro Claude Code)

## Jak funguje

Skill zkontroluje PDF tvé práce podle pravidel v [`docs/pravidla/`](../../../docs/pravidla/README.md)
(formát, struktura, úvod, závěr, abstrakt, citace, odborný styl). Skript
`vytahni.py` vytáhne z PDF přesná fakta — písmo, velikost, tučnost, polohy
řádků — a Claude je porovná s pravidly; obsah posoudí z textu a některé věci
ověří přímo v `src/*.tex` a v logu překladu. Výsledkem je hlášení s ID pravidel
v `output/kontrola_<datum>.md`.

Hlavní agent si práci zmapuje a sám zkontroluje věci přes celou práci (záhlaví,
číslování, rozsah). Jednotlivé části (úvodní strany, úvod a závěr, kapitoly,
literatura…) předá souběžně subagentům `kontrola-casti`
([`.claude/agents/`](../../agents/kontrola-casti.md)), každému jen jeho strany
a pravidla, a jejich nálezy sloučí. Subagent nemá nástroje na úpravu souborů.
Celá kontrola tak spotřebuje víc tokenů než kontrola jedné části — když
narážíš na limit, kontroluj po částech nebo napiš `bez subagentů`.

Skill **jen upozorňuje** a nic v práci nemění — odpovídá stupni 2 (Asistence)
podle [MP č. 8/2026](../../../Dokumenty/MP%208-2026%20Metodický%20pokyn%20k%20užívání%20AI%20na%20VŠPJ.pdf),
který je u závěrečné práce nejvyšší přípustný, pokud vedoucí nestanovil jinak —
ověř si to u vedoucího. Využití AI v práci nezapomeň deklarovat.

## Jak ho přidat

1. Forkni repozitář a naklonuj si ho (viz hlavní [README](../../../README.md)).
2. Nainstaluj [Claude Code](https://docs.claude.com/en/docs/claude-code) a spusť ho
   v kořeni repozitáře — skill se načte sám (je ve složce `.claude/skills/`).
3. Nainstaluj knihovnu pro čtení PDF do virtuálního prostředí v kořeni repa
   (skill ho najde sám, `.venv/` se necommituje):
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install pymupdf          # Linux, macOS
   .venv\Scripts\pip install pymupdf      # Windows
   ```
   Bez ní skill funguje jen přibližně (PDF prohlíží jako obrázky).

## Jak ho použít

1. Sestav PDF: `./build.sh` (do `output/`), nebo ho stáhni z `Verze/` po
   pushi (GitHub Actions).
2. V Claude Code napiš třeba:
   - `zkontroluj práci` nebo `/kontrola-prace` — celá práce,
   - `zkontroluj úvod`, `zkontroluj citace`, `zkontroluj titulní stranu`,
   - `zkontroluj jen formální pravidla`.
3. Hlášení najdeš v `output/kontrola_<datum>.md` (složka `output/` se
   necommituje). Nálezy jsou rozdělené na **chyby**, **upozornění**
   (doporučení a posouzení — rozhodni sám) a **poznámky**.

Text práce se při kontrole zpracovává AI. Osobní, důvěrné a jinak chráněné
údaje (data respondentů, obchodní tajemství) do práce v době kontroly nedávej
nebo je anonymizuj (MP č. 8/2026, čl. 3).

Chybu v pravidle nebo ve skillu nahlas issue nebo pošli PR do hlavního
repozitáře. Testy skillu (potřebují i pytest: `.venv/bin/pip install pytest`):
`.venv/bin/python -m pytest -q .claude/skills/kontrola-prace`.
