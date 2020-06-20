'''
from tkinter import *
win = Tk()
win.title('모달 제목')
win.geometry("200x200+300+30")
btn = Button(win, text="버튼")
btn.place(x=20, y=20)
win.mainloop()
'''

from tkinter import *

root = Tk()


lb = Label(root, text="이름")
lb.pack()
 
txt = Entry(root)
txt.pack()
 
btn = Button(root, text="OK")
btn.pack()


root.mainloop()
# 기본 실행



