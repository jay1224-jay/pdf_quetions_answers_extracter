import os
from PyPDF2 import PdfReader


files = [ x for x in os.listdir(".") if ".pdf" in x ]



for file in files:
    # print("current:",  file)

    
    os.system("pdftotext '{}'".format(file))
    text = ""
    
    try:
        with open("{}.txt".format(file[:-4]), "r") as f:
            text = f.read()
    except:
        continue
        

    if "測驗題部分" in text:
        print("multiple")
        os.system("mv \'"+file+"\' multiple_choice")
    elif "英文" in file:
        print("english")
        os.system("mv \'"+file+"\' english")

    os.system("rm '{}.txt'".format(file[:-4]))



