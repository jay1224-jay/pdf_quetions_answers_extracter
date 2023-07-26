
from PyPDF2 import PdfReader
import pdfplumber
import os


chinese = "一、 二、 三、 四、 五、 六、 七、 八、 九、 十、".split()
numeric = [ x for x in range(1, 11) ]

trans = {}

for i in range(len(chinese)):
    trans[numeric[i]] = chinese[i]


class extract:

    def __init__(self):


        filenames = self.get_pdf()

        for filename in filenames:
            pages = self.get_page(filename)

            self.quetions = []
            self.answers = []
            self.all_text = ""

            for page in pages:
                self.all_text += page.extract_text()

            # print(self.all_text)
            print("\n\n\n")
            self.get_q(self.all_text)

            #for index, item in enumerate(self.quetions, 1):
            #    print(index, item, end="\n\n")

            self.q2csv(self.quetions, self.answers, filename)

            print("start")
            for q, a in zip(self.quetions, self.answers):
                print("que\n", q, "\nans\n", a, end="\n\n")
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

        # preprocessing: remove comma from text
        text = text.replace(",", " ")

        text = text[text.find("一、")+2:]
        
        #for j in range(10):
        count = 1
        while 1:
            n = text.find("答：")
            if n == -1:
                break
            i = 0
            for i in range(n, 0, -1): # find quetion end
                if text[i:i+2] == "分）":
                    break
            i -= 3 # remove (25分)

            que = self.text_clean(self.text_remove_esc(text[:i]))
            print("current:", que)
            self.quetions.append(que)

            text = text[i:]

            ans_begin = text.find("答：") + 2

            text = text[ans_begin:]
            
            try:
                ans_end = text.find(trans[count+1]) - 1
                if ans_end == -2: # ans_end == -1
                    ans_end = text.find(trans[count+1][0]  + "\n" + trans[count+1][1]) - 2 
            except:
                return

            ans = self.text_clean(text[:ans_end])
            print("ans: " + ans)
            self.answers.append(ans.replace("\n", ""))
            text = text[ans_end+3:]
            
            count += 1

        #　return text[qstart:]

    def text_remove_esc(self, text):
        return text.replace("\n", "")

    def q2csv(self, quetions, answers, filename):
        with open(filename[:-4] + ".csv", "w") as f:
            for q, a in zip(quetions, answers):
                if q == "":
                    continue
                f.write(q + ", " +  a + "\n")

    def replace_abcd(self, text):
        d = {"/onesans" : "(A)", "/twosans": "(B)", "/threesans":"(C)", "/foursans":"(D)"}

        for k, v in d.items():
            text = text.replace(k, v)

        return text

    def text_clean(self, text):
        remove_word = ["【版權所有，重製必究！】", '地方特考高分詳解', '高點', '高上公職', '--', '高上', '‧',
                        '   ', '考點命中', '《透明的刑法總則編 》', '高點文化出版', '高點文化出版', '【版權所有，重製必',
                        '02-23318268']

        for word in remove_word:
            text = text.replace(word, "")

        return text



extract()
