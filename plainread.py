
from PyPDF2 import PdfReader
import pdfplumber
import os

class extract:

    def __init__(self):

        filenames = self.get_pdf()

        for filename in filenames:
            pages = self.get_page(filename)

            self.quetions = []
            self.all_text = ""

            for page in pages:
                self.all_text += page.extract_text()

            print(self.all_text)
            # print(self.all_text)
            print("\n\n\n")

            print("done")

    def get_pdf(self):
        return [ x for x in os.listdir(".") if "pdf" in x ]

    def get_page(self, filename):
        reader = PdfReader(filename)
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        # text = page.extract_text()

        return reader.pages

    def get_q(self, text):
        
        while True:
            qstart = text.find("題目") # index
            if qstart == -1: # cannot find target
                qstart = text.find(")")
                if qstart == -1:
                    break
                s = qstart
            else:
                text = text[qstart:]
                
                s = text.find("\n")
            text = text[s:]
            end = text.find("【")
            quetion = self.text_remove_esc(text[:end])
            text = text[end:]

            self.quetions.append(quetion)

        #　return text[qstart:]

    def text_remove_esc(self, text):
        return text.replace("\n", "")

    def q2csv(self, quetions, filename):
        with open(filename[:-4] + ".csv", "w") as f:
            for q in quetions:
                f.write(q + ", " + "\n")



extract()
