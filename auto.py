import os


pdfs = [ x for x in os.listdir(".") if ".pdf" in x ]

for pdf in pdfs:
    print("current process pdf name:", pdf)
    os.system("open " + pdf)
    os.system("python3 r.py " + pdf)
