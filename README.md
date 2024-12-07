# PDF to Excel OCR Processor

Dieses Python-Skript extrahiert Datumsangaben und zugehörigen Text aus PDF-Dateien mithilfe von OCR und speichert die Ergebnisse in einer Excel-Datei.

## Anforderungen

- **Python Version**: 3.7 oder höher  
- **Python-Bibliotheken**:
  - `pdf2image`
  - `pytesseract`
  - `Pillow`
  - `pandas`
  - `openpyxl`
- **Zusätzliche Tools**:
  - [Poppler für Windows](https://github.com/oschwartz10612/poppler-windows/releases/tag/v24.08.0-0)
  - [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

## Installation

### 1. Python-Bibliotheken installieren
```bash
pip install pdf2image pytesseract pillow pandas openpyxl
