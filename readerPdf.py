from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time
import re
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r".\Downloads\ocr\tesseract.exe"

pdf_path = "pdfTest2.pdf"
poppler_path = r".\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"

def preprocess_image(image):
    img = image.convert("L")
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    return img


def split_text(text):
    pattern = r'(\d{4}\s+\d{1,2}\.\w+\.?:|\d{4}\s+\w+\.?(?:/\w+\.?)?:)\s*(.*?)(?=\n\d{4}\s|\Z)'
    matches = re.findall(pattern, text, re.DOTALL)
    return [[match[0], match[1].strip()] for match in matches]

try:
    pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    print(f"{len(pages)} Seiten erfolgreich aus der PDF extrahiert.")
    time.sleep(1)
except Exception as e:
    print("Fehler beim Konvertieren der PDF in Bilder:", e)
    exit()

all_data = []

for i, page in enumerate(pages, start=1):
    try:
        processed_page = preprocess_image(page)
        custom_config = r'--oem 3 --psm 6'
        text = image_to_string(processed_page, lang="deu", config=custom_config)

        page_data = split_text(text)

        for datum, inhalt in page_data:
            all_data.append([datum, inhalt])

        print(f"Seite {i} erfolgreich verarbeitet.")
        time.sleep(1)
    except Exception as e:
        print(f"Fehler beim Lesen von Seite {i}:", e)
try:
    df = pd.DataFrame(all_data, columns=["Datum", "Text"])
    output_path = "output.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Excel-Datei erfolgreich erstellt: {output_path}")
except Exception as e:
    print("Fehler beim Erstellen der Excel-Datei:", e)
