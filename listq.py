

import tkinter as tk
import clipboard



def done():
    with open(filename + ".csv", "w") as f:
        for i in range(len(q_list)):
            f.write("{}, {}\n".format(q_list[i], a_list[i]))


def clean():
    text.delete(0, tk.END)

def gen():
    out = text.get().replace("\n", "")
    clean()

    for i in range(20):
        start = out.find(".")
        out = out[start+1:]
        end = out.find(".")
        print(out[:end-2].replace("\n", "").replace("     ", "_____") + ", ", end="\n\n\n")
        out = out[end:]

    # clipboard.copy(out)

win = tk.Tk()
win.title("reformat list quetions")
win.geometry("400x300")


text = tk.Entry(win, width=30)
text.pack()


clear_b = tk.Button(win, text="clear", command=clean)
clear_b.pack()

l = tk.Button(win, text="generate", command=gen)
l.pack()


win.mainloop()
