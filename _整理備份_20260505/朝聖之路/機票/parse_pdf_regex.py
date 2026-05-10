import sys
import re
from pypdf import PdfReader

for pdf_path in sys.argv[1:]:
    print(f"\n--- {pdf_path} ---")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    # Extract flight numbers and times
    flights = re.findall(r'([A-Z0-9]{2}\s*\d{2,4})\s*(\d{2}\s*[A-Z][a-z]{2}\s*\d{4}|\d{2}\s*[A-Z][a-z]{2})\s*(\d{2}:\d{2})\s*(\d{2}\s*[A-Z][a-z]{2}\s*\d{4}|\d{2}\s*[A-Z][a-z]{2})?\s*(\d{2}:\d{2})?', text)
    print("Found potential flights:", flights)
    
    # Let's just print lines containing "Jun", "BR", "TP", ":", "LHR", "LIS", "OPO", "TPE"
    lines = text.split('\n')
    for line in lines:
        if any(x in line for x in ['Jun', 'BR ', 'TP ', ':', 'LHR', 'LIS', 'OPO', 'TPE', 'LONDON', 'TAIPEI', 'PORTO']):
            print(line.strip())
