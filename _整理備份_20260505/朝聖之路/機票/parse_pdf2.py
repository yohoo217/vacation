import sys
from pypdf import PdfReader
import re

for pdf_path in sys.argv[1:]:
    print(f"\n--- {pdf_path} ---")
    reader = PdfReader(pdf_path)
    text = reader.pages[0].extract_text()
    
    lines = text.split('\n')
    for line in lines[:60]:
        print(line.strip())
