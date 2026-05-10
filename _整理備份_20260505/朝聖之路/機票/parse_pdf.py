import sys
from pypdf import PdfReader
for pdf_path in sys.argv[1:]:
    print(f"--- {pdf_path} ---")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    print(text)
