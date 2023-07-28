import os

s = [ x for x in os.listdir(".") if ".csv" in x ]

for f in s:
    print("move:", f)
    os.system("mv " + f + " ../../csv_files")
