import tkinter as tk
import clipboard
import sys


q_list = []
a_list = []
if len(sys.argv) < 2:
    filename = input("csv file name( no .csv ):  ")
else:
    filename = sys.argv[1]

if ".pdf" in filename:
    filename = filename[:-4]

def done():
    with open(filename + ".csv", "w") as f:
        for i in range(len(q_list)):
            f.write("{}, {}\n".format(q_list[i], a_list[i]))


def clean():
    q.delete(0, tk.END)
    a.delete(0, tk.END)

def send():
    q_text = q.get().replace("\n", "")
    a_text = a.get().replace("\n", "")
    clean()
    q_list.append(q_text)
    a_list.append(a_text)
    print(q_text, a_text)

win = tk.Tk()
win.title("line break remover")
win.geometry("400x300")

tk.Label(win, text="quetion: ").grid(row=0, column=0)

q = tk.Entry(win, width=30)
q.grid(row=0, column=1)

tk.Label(win, text="answer: ").grid(row=1, column=0)

a = tk.Entry(win, width=30)
a.grid(row=1, column=1)


do = tk.Button(win, text="clear", command=clean)
do.grid(row=2, column=0)
l = tk.Button(win, text="send", command=send)
l.grid(row=2, column=1)

don = tk.Button(win, text="done", command=done)
don.grid(row=3, column=0)

win.mainloop()
