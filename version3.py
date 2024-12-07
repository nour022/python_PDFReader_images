from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time
import re

pytesseract.pytesseract.tesseract_cmd = r"D:\ocr\tesseract.exe"

pdf_path = "pdfTest2.pdf"
poppler_path = r"C:\Users\mnour\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"

def preprocess_image(image):
    img = image.convert("L")  # Graustufen
    img = img.filter(ImageFilter.MedianFilter())  # Rauschen entfernen
    enhancer = ImageEnhance.Contrast(img)  # Kontrast erhöhen
    img = enhancer.enhance(2)  # Kontrast verdoppeln
    return img


def split_data(text):
    pattern = r'(\d{4}\s+\d{1,2}\.\w+\.?:|\d{4}\s+\w+\.?(?:/\w+\.?)?:)'
    text = re.findall(pattern, text)

    return text


def split_text(text):
    # Regex-Muster, um Datum und zugehörigen Text zu erfassen
    pattern = r'(\d{4}\s+\d{1,2}\.\w+\.?:|\d{4}\s+\w+\.?(?:/\w+\.?)?:)\s*(.*?)(?=\n\d{4}\s|\Z)'

    # Suche nach allen Matches mit Datum und zugehörigem Text
    matches = re.findall(pattern, text, re.DOTALL)

    # Ergebnisse formatieren
    result = [[match[0], match[1].strip()] for match in matches]

    return result


try:
    pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    print(f"{len(pages)} Seiten erfolgreich aus der PDF extrahiert.")
    time.sleep(1)
except Exception as e:
    print("Fehler beim Konvertieren der PDF in Bilder:", e)
    exit()

for i, page in enumerate(pages, start=1):
    try:
        processed_page = preprocess_image(page)
        custom_config = r'--oem 3 --psm 6'
        text = image_to_string(processed_page, lang="deu", config=custom_config)
        data = split_data(text)
        text = split_text(text)

        print(f"Seite {i}:\n{data}\n\n{text}\n")
        time.sleep(3)
    except Exception as e:
        print(f"Fehler beim Lesen von Seite {i}:", e)
