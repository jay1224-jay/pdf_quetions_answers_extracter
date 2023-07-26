"""
from PyPDF2 import PdfReader



reader = PdfReader("1.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)
"""
import pdfplumber

with pdfplumber.open("7.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.lines)
