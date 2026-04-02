import os
import pdfplumber
import json
from groq import Groq
from dotenv import load_dotenv

# Kulcs betöltése
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_text_from_pdf(pdf_path):
    """Kinyeri a nyers szöveget a PDF fájlból."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += str(page.extract_text()) + "\n"
        return text
    except Exception as e:
        return f"Hiba a PDF olvasásakor: {e}"


def analyze_invoice_with_ai(raw_text):
    """A Groq AI segítségével strukturált adatokat készít."""
    prompt = f"""
    Az alábbi szöveg egy számlából származik. 
    Kérlek, nyerd ki belőle a következő adatokat JSON formátumban:
    - elado_neve
    - vevo_neve
    - szamla_szama
    - kiallitas_datuma
    - vegosszeg_brutto
    - penznem

    Szöveg:
    {raw_text}
    """

    # Itt a Llama-3 modellt használjuk, ami ingyenes és profi
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Te egy JSON adatkinyerő asszisztens vagy. Csak tiszta JSON-t válaszolj!"},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content


def main():
    pdf_file = "szamla_pelda.pdf"

    if not os.path.exists(pdf_file):
        print(f"Hiba: A {pdf_file} nem található!")
        return

    print("--- 1. Szöveg kinyerése a PDF-ből... ---")
    raw_content = extract_text_from_pdf(pdf_file)

    if len(raw_content.strip()) < 10:
        print("Hiba: Nem sikerült elég szöveget kinyerni a PDF-ből.")
        return

    print("--- 2. Adatfeldolgozás AI-val (Groq)... ---")
    try:
        structured_data = analyze_invoice_with_ai(raw_content)

        # Eredmény mentése
        with open("eredmeny.json", "w", encoding="utf-8") as f:
            f.write(structured_data)

        print("--- KÉSZ! Az eredmény: ---")
        print(structured_data)
    except Exception as e:
        print(f"Hiba történt az AI feldolgozás során: {e}")


if __name__ == "__main__":
    main()
