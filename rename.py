import os

csvs = [ x for x in os.listdir(".") if ".csv" in x ]

for csv in csvs:
    print("current:", csv)
    os.system("mv {} {}".format(csv, "選擇題" + csv))
