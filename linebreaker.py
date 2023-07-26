
import tkinter as tk
import clipboard
import sys



def done():
    with open(filename + ".csv", "w") as f:
        for i in range(len(q_list)):
            f.write("{}, {}\n".format(q_list[i], a_list[i]))


def clean():
    text.delete(0, tk.END)

def remove():
    out = text.get().replace("\n", "")
    clean()
    print(out)
    clipboard.copy(out)

win = tk.Tk()
win.title("line break remover")
win.geometry("400x300")


text = tk.Entry(win, width=30)
text.pack()


clear_b = tk.Button(win, text="clear", command=clean)
clear_b.pack()

l = tk.Button(win, text="linebreak remove", command=remove)
l.pack()


win.mainloop()
