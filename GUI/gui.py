from tkinter import *
win = Tk()
win.title('모달 제목')
win.geometry("200x200+300+30")
btn = Button(win, text="버튼")
btn.place(x=20, y=20)
win.mainloop()