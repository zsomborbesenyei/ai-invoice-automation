# Multi-Format AI Invoice Parser (OCR + LLM)

Ez egy intelligens automatizációs eszköz, amely képes strukturálatlan számlákból (PDF, PNG, JPG) adatokat kinyerni és JSON formátumba rendezni.

### Főbb funkciók:
- **Dinamikus fájlkezelés**: A szkript automatikusan felismeri és feldolgozza a mappában lévő összes támogatott fájlt.
- **Hibrid technológia**: PDF-parszolás és Tesseract OCR kombinációja.
- **Llama-3 LLM integráció**: A Groq felhőjén keresztül az AI értelmezi a szöveget, nem csak beolvassa.

### Kinyert adatok:
A rendszer az alábbi mezőket azonosítja:
`elado_neve`, `vevo_neve`, `szamla_szama`, `kiallitas_datuma`, `vegosszeg_brutto`, `penznem`.

### Technológiai stack:
- **Python** 
- **Groq API** 
- **Tesseract OCR** 
- **pdfplumber** 
