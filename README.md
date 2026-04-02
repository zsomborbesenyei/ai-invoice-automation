# AI Invoice Parser (OCR + GPT-4)

Ez egy Python alapú automatizációs eszköz, amely képes strukturálatlan PDF számlákból kulcsfontosságú adatokat kinyerni és JSON formátumba rendezni.

## Hogyan működik?
1. Beolvassa a PDF fájlt a `pdfplumber` könyvtár segítségével.
2. A kinyert szöveget továbbítja az OpenAI GPT-4o-mini modelljének.
3. Az AI felismeri az eladót, a végösszeget, a dátumot és a pénznemet.
4. Az eredményt egy strukturált `eredmeny.json` fájlba menti.

## Telepítés és használat
1. Klónozd a projektet.
2. Telepítsd a függőségeket: `pip install -r requirements.txt`.
3. Hozz létre egy `.env` fájlt és add hozzá az `OPENAI_API_KEY` kulcsodat.
4. Futtasd a programot: `python main.py`.

## Miért hasznos ez?
Ez a script kiváltja a manuális adatrögzítést, csökkenti a hibázási lehetőséget és skálázhatóvá teszi a számlafeldolgozást bármilyen vállalat számára.
