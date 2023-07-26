import os

csv_file = [ x for x in os.listdir(".") if ".csv" in x ]

print("csv filename, comma count")

for csv in csv_file:
    print(csv, end=",  ")

    with open(csv, 'r') as f:
        print(f.read().count(","))
