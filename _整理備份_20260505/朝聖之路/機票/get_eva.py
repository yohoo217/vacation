import pdfplumber
import sys

for pdf_path in sys.argv[1:]:
    with pdfplumber.open(pdf_path) as pdf:
        text = pdf.pages[0].extract_text()
        print(f"\n--- {pdf_path} ---")
        for line in text.split('\n'):
            if 'BR6' in line or 'BR 6' in line or 'JUN' in line or 'JUL' in line or 'MAY' in line:
                print(line)
