import os
import pdfplumber
import json
from openai import OpenAI
from dotenv import load_dotenv

# API kulcs betöltése a .env fájlból
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_text_from_pdf(pdf_path):
    """Kinyeri a nyers szöveget a PDF fájlból."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def analyze_invoice_with_ai(raw_text):
    """A GPT-4 segítségével strukturált adatokat készít a nyers szövegből."""
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

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Gyors és olcsóbb teszteléshez
        messages=[{"role": "system", "content": "Te egy precíz adatfeldolgozó asszisztens vagy."},
                  {"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content


def main():
    pdf_file = "szamla_pelda.pdf"  # Ide tedd a teszt PDF-edet

    if not os.path.exists(pdf_file):
        print(f"Hiba: A {pdf_file} nem található!")
        return

    print("--- 1. Szöveg kinyerése a PDF-ből... ---")
    raw_content = extract_text_from_pdf(pdf_file)

    print("--- 2. Adatfeldolgozás AI-val... ---")
    structured_data = analyze_invoice_with_ai(raw_content)

    # Eredmény mentése fájlba
    with open("eredmeny.json", "w", encoding="utf-8") as f:
        f.write(structured_data)

    print("--- Kész! Az adatok mentve az eredmeny.json fájlba. ---")
    print(structured_data)


if __name__ == "__main__":
    main()
