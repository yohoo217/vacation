import sys
import pdfplumber

for pdf_path in sys.argv[1:]:
    print(f"\n--- {pdf_path} ---")
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        print(text)
