import pdfplumber
import sys
import re

for pdf_path in sys.argv[1:]:
    with pdfplumber.open(pdf_path) as pdf:
        text = pdf.pages[0].extract_text()
        print(f"\n--- {pdf_path} ---")
        for line in text.split('\n'):
            if any(x in line for x in ['BR', 'TP', 'LONDON', 'TAIPEI', 'PORTO', 'BANGKOK']):
                print(line)
