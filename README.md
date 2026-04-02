# AI-Powered Invoice Parser (Groq & Llama 3)

Ez egy Python alapú automatizációs eszköz, amely képes bármilyen PDF formátumú számlából kinyerni a kulcsfontosságú adatokat és azokat strukturált JSON formátumba rendezni.

## Miért különleges?
A legtöbb hagyományos szoftver elbukik, ha megváltozik a számla elrendezése. Ez a megoldás viszont **Large Language Model (LLM)** technológiát használ, így rugalmasan felismeri az adatokat akkor is, ha a beszállító új sablont használ.

## Technikai részletek
- **Nyelv:** Python
- **AI Modell:** Llama-3.3-70b (a Groq felhőjén keresztül)
- **PDF Feldolgozás:** `pdfplumber`
- **Adatformátum:** Strukturált JSON

## Telepítés és használat
1. Klónozd a repository-t.
2. Telepítsd a függőségeket:  
   `pip install -r requirements.txt`
3. Hozz létre egy `.env` fájlt a saját Groq API kulcsoddal:  
   `GROQ_API_KEY=a_te_kulcsod`
4. Helyezz el egy `szamla_pelda.pdf` fájlt a mappában.
5. Futtasd:  
   `python main.py`

## Jövőbeli tervek
- Webes felület (Streamlit) hozzáadása.
- Több számla tömeges (batch) feldolgozása.
- Google Sheets integráció az adatok automatikus mentéséhez.
