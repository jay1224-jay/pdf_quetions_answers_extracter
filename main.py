from PyPDF2 import PdfReader
import pdfplumber
import os

class extract:

    def __init__(self):


        filenames = ["test.txt"] # self.get_pdf()

        for filename in filenames:
            #pages = self.get_page(filename)

            self.quetions = []
            self.all_text = ""
            with open("test.txt", "r") as f:
                self.all_text = f.read()

            #for page in pages:
            #    self.all_text += page.extract_text()

            # print(self.all_text)
            print("\n\n\n")
            self.get_q(self.all_text)

            for index, item in enumerate(self.quetions, 1):
                print(index, item, end="\n\n")

            self.q2csv(self.quetions, filename)

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

        text = text[text.find("1.")+2:]
        
        #for j in range(10):
        count = 0
        while 1:
            count += 1
            n = text.find(".")
            if n == -1:
                break
            i = 0
            for i in range(n, 0, -1): # find quetion end
                if text[i] == "\n":
                    break
            que = self.replace_abcd(self.text_remove_esc(text[:i]))
            print("current:", que)
            self.quetions.append(que)
            if count <= 8:
                text = text[i+3:]
            else:
                text = text[i+4:]

        #　return text[qstart:]

    def text_remove_esc(self, text):
        return text.replace("\n", "")

    def q2csv(self, quetions, filename):
        with open(filename[:-4] + ".csv", "w") as f:
            for q in quetions:
                f.write(q + ", " + "\n")

    def replace_abcd(self, text):
        d = {"/onesans" : "(A)", "/twosans": "(B)", "/threesans":"(C)", "/foursans":"(D)"}

        for k, v in d.items():
            text = text.replace(k, v)

        return text



extract()
