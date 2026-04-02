import os
import pdfplumber
import pytesseract
from PIL import Image
from groq import Groq
from dotenv import load_dotenv
import json

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SUPPORTED_EXTENSIONS = ['.pdf', '.png', '.jpg', '.jpeg']

def extract_text(file_path):
    """Szöveg kinyerése PDF-ből vagy képből (PNG/JPG)."""
    ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if ext == ".pdf":
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += str(page.extract_text()) + "\n"
            return text
        
        elif ext in ['.png', '.jpg', '.jpeg']:
            img = Image.open(file_path)
            return pytesseract.image_to_string(img, lang='hun+eng')
    except Exception as e:
        print(f"Hiba a fájl beolvasásakor ({file_path}): {e}")
    return None

def analyze_with_ai(raw_text, filename):
    """Adatkinyerés AI-val a pontosan kért mezőkkel."""
    
    prompt = f"""
    Feladat: Nyerd ki az alábbi szövegből a számla adatait szigorúan JSON formátumban.
    Ha egy adat nem található, írj 'N/A'-t az értékhez.
    
    Kérem az alábbi mezőket:
    - elado_neve
    - vevo_neve
    - szamla_szama
    - kiallitas_datuma
    - vegosszeg_brutto
    - penznem

    A feldolgozandó szöveg:
    {raw_text}
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Te egy precíz adatfeldolgozó vagy, aki csak JSON-t válaszol."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Hiba az AI elemzés során: {e}"

def main():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    found_any = False
    print("=== AI SZÁMLA FELDOLGOZÓ INDÍTÁSA ===")

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in SUPPORTED_EXTENSIONS:
            found_any = True
            print(f"\n[+] Feldolgozás: {file}")
            
            raw_content = extract_text(file)
            
            if raw_content and len(raw_content.strip()) > 5:
                json_result = analyze_with_ai(raw_content, file)
                
                print("--- Kinyert adatok: ---")
                print(json_result)
                
                output_name = f"eredmeny_{file}.json"
                with open(output_name, "w", encoding="utf-8") as f:
                    f.write(json_result)
                print(f"Mentve: {output_name}")
            else:
                print(f"[-] {file}: Nem található szöveg vagy a fájl olvashatatlan.")

    if not found_any:
        print("Nincs feldolgozható fájl (.pdf, .png, .jpg) a mappában!")

if __name__ == "__main__":
    main()
