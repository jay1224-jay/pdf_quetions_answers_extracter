
from PyPDF2 import PdfReader
import pdfplumber
import os


chinese = "一、 二、 三、 四、 五、 六、 七、 八、 九、 十、".split()
                     
numeric = [ x for x in range(1, 11) ]

trans = {}

for i in range(len(chinese)):
    trans[numeric[i]] = chinese[i]


for pdf in [ x for x in os.listdir(".") if "pdf" in x ]:
    if "(" in pdf or ")" in pdf:
        print("rename")
        os.system("mv \'{}\' \'{}\'".format(pdf, pdf.replace("(", "_").replace(")", "_")) )


class extract:

    def __init__(self):


        filenames = self.get_pdf()


        for filename in filenames:

            print("current file:", filename)
            self.quetions = []
            self.answers = []
            self.all_text = ""

            os.system("pdftotext '{}'".format(filename))
            with open("{}.txt".format(filename[:-4]), "r") as f:
                self.all_text = f.read()

            os.system("rm '" + filename[:-4]+".txt'")

            # print(self.all_text)
            # pages = self.get_page(filename)
            # for page in pages:
            #     self.all_text += page.extract_text()

            # print(self.all_text)

            self.exam_year = filename[:-4].split('_')[-1]

            self.get_q(self.all_text)

            #for index, item in enumerate(self.quetions, 1):
            #    print(index, item, end="\n\n")

            self.q2csv(self.quetions, self.answers, filename)

            #for q, a in zip(self.quetions, self.answers):
            #    print("que\n", q, "\nans\n", a, end="\n\n")
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
        # alternative:
        # t = text.find("答：")

        
        if "【擬答】" in text:
            count = 1
            while 1:
                n = text.find("【擬答】")
                # print(n)
                if n == -1:
                    break
                i = 0
                # print(text)
                for i in range(n, 0, -1): # find quetion end
                    if text[i:i+2] == "分）" or text[i:i+2] == "分)":
                        break
                i -= 4 # remove (25分)

                que = self.text_clean(text[:i].replace("\n", ""))
                # print("current:", que)
                self.quetions.append(que)

                text = text[i:]

                # print("finding")
                ans_begin = text.find("【擬答】") + 4
                if ans_begin == 1: # ans_begin == -1
                    print("cannot find answer")

                text = text[ans_begin:]
                
                try:
                    ans_end = text.find(trans[count+1]) - 1
                    if ans_end == -2: # ans_end == -1
                        ans_end = text.find(trans[count+1][0]  + "\n" + trans[count+1][1]) - 2 
                except:
                    return

                ans = self.text_clean(text[:ans_end].replace("\n", ""))
                # print("ans: " + ans)
                self.answers.append(ans)
                text = text[ans_end+3:]
                
                count += 1

        else:
            count = 1
            while 1:
                n = text.find("答：")
                if n == -1:
                    break
                i = 0
                for i in range(n, 0, -1): # find quetion end
                    if text[i:i+2] == "分）":
                        break
                i -= 4 # remove (25分)

                que = self.text_clean(text[:i].replace("\n", ""))
                self.quetions.append(que)

                text = text[i:]

                ans_begin = text.find("答：") + 2

                text = text[ans_begin:]
                
                try:
                    ans_end = text.find(trans[count+1]) - 1
                    if ans_end == -2: # ans_end == -1
                        # print("find -1")
                        ans_end = text.find(trans[count+1][0]  + "\n" + trans[count+1][1]) - 2 
                except:
                    return

                ans = self.text_clean(text[:ans_end].replace("\n", ""))
                
                # print("current:", que)
                # print("ans: " + ans)
                self.answers.append(ans)
                text = text[ans_end+3:]
                
                count += 1

        #　return text[qstart:]

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
        target = "高點‧高上高普特考 goldensun.get. com.tw 台北市開封街一段 2號 8 樓  02-23318268  【中壢】 中壢市中山路100號14樓‧03-4256899       【台中】 台中市東區復興路四段231-3號 1樓‧04-22298699【台南】台南市中西區中山路147號 3樓之1‧06-2235868 【高雄】高雄市新興區中山一路308 號8樓‧07-2358996【另有板橋‧淡水‧三峽‧林口‧羅東‧逢甲‧東海‧中技‧彰化‧嘉義】"
        remove_word = [
                '高上高普特考 www.get.com.tw/goldensun 台北市開封街一段 2 號 8 樓02-23318268【中壢】中壢市中山路 100 號 14 樓 03-4256899【台中】台中市東區復興路四段 231-3 號 1 樓‧04-22298699【台南】台南市中西區中山路 147 號 3 樓之 1‧06-2235868 【高雄】高雄市新興區中山一路 308 號 8 樓‧07-2358996【另有淡水‧三峽‧林口‧羅東‧中壢‧逢甲‧東海‧中技】',
                '高點律師司法官班', 'http://www.license.com.tw', '(代表號)',
                target,
                "高上高普特考 www.get.com.tw/goldensun 台北市開封街一段 2 號 8 樓02-23318268【中壢】中壢市中山路 100 號 14 樓 03-4256899【台中】台中市東區復興路四段 231-3 號 1 樓‧04-22298699【台南】台南市中西區中山路 147 號 3 樓之 1‧06-2235868 【高雄】高雄市新興區中山一路 308 號 8 樓‧07-2358996【另有淡水‧三峽‧林口‧羅東‧中壢‧逢甲‧東海‧中技】",
                "台北市開封街一段",
                "2 號 7 樓電話", "02-23115586", "http://www.license.com.tw/lawyer",
                "【版權所有，重製必究！】", "【版權所有，重製必究", '【法律專班】', '地方特考高分詳解', 
                '高點', '高上公職', '--', '高上', '‧', '版權所有，重製必究！',
                '   ', '  ', '考點命中', '《透明的刑法總則編 》', '高點文化出版', 
                '02-23318268', "－", '司法三等全套詳解', '【法律專班】',
                '【版權所有，重製必', '【參考書目】', '《保險法實例研習》', '', '', '', self.exam_year, "【高分閱讀】", '高普考高分詳解', '【參考資料】', '北市開封街一段 2 號 7 樓', '律師司法官班' 
                ]
        for word in remove_word:
            text = text.replace(word, "")

        return text



extract()


csv_file = [ x for x in os.listdir(".") if ".csv" in x ]

print(" ======== testing =========")

print("csv filename, comma count")

for csv in csv_file:
    print(csv, end=",  ")

    with open(csv, 'r') as f:
        c = f.read().count(",")
        print(c, end=",  ")

        if c < 2:
            print("=== warning ===")
            os.system("mv '{}' problem".format(csv[:-4] + ".pdf"))
            os.system("rm '{}'".format(csv))
        else:
            print()


# 一)如 A 棟大樓之全體所有人甲 1 －甲 25 共二十五人，依消費者保護法第五十條規定，將其對房屋出賣人乙及建築師丙之損害賠償請求權讓與丁文教基金會，丁乃以乙及丙為被告，起訴請求乙、丙連帶賠償損害。其後，甲 1 又基於其房屋震毀之原因事實，以乙及丙為被告，起訴請求乙、丙連帶賠償損害。試問：甲 1是否為適格當事人？法院應為如何之判決？(二)如 A 棟大樓之全體所有人甲 1 －甲 25 共二十五人共同起訴，以乙及丙為共同被告，請求乙及丙連帶賠償原告所受損害。訴訟繫屬後，全體共同原告選定甲 1 為當事人。隨後，原告甲 2 於訴訟繫屬中死亡，其繼承人戊向法院聲明承受訴訟。試問：甲 2 之死亡是否影響甲 1 被選定人之資格？戊得否承受訴訟？
