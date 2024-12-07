from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import pytesseract
import  time
pytesseract.pytesseract.tesseract_cmd = r"D:\ocr\tesseract.exe"

pdf_path = "pdfTest.pdf"

poppler_path = r"C:\Users\mnour\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"

try:
    pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    print(f"{len(pages)} Seiten erfolgreich aus der PDF extrahiert.")
    time.sleep(1)
except Exception as e:
    print("Fehler beim Konvertieren der PDF in Bilder:", e)
    exit()

# OCR auf jede Seite anwenden
for i, page in enumerate(pages, start=1):
    try:
        text = image_to_string(page, lang="deu")
        print(f"Seite {i}:\n{text}\n")
        time.sleep(3)
    except Exception as e:
        print(f"Fehler beim Lesen von Seite {i}:", e)
