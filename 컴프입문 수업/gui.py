from tkinter import *

def enter(label):
    if label == "C":
        entry.delete(0, END)
        entry.insert(0, '0')
    elif label == "D":
        val = eval(entry.get())
        val *= 2
        entry.delete(0, END)
        entry.insert(0, val)
    elif entry.get() == "0":
        entry.delete(0, END)
        entry.insert(END, label)

def main():
    global entry 
    window = Tk()
    entry = Entry(window, width=12, justify=RIGHT)
    entry.insert(0, '0')
    entry.pack()
    frm = Frame(window)
    frm.pack()

    for label in '10CD':
        btn = Button(frm, text=label, width=3,
                        command=(lambda char=label: enter(char)))
        btn.pack(side=LEFT)
    window.mainloop()
if __name__ == "__main__":
    entry = None
    main()
    line = input()
 

        