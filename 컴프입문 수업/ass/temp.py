# GUI 계산기 만들기 * 제한사항 : class 사용

from tkinter import *
from tkinter import ttk
 
op = ''  
temp_num = 0
is_answer = False
 
def press(value):
    global temp_num
    global is_answer
    if value=='C':
        num_entry.delete(0,'end')
        op = ''
        is_answer = False
    else:
        if is_answer:
            num_entry.delete(0,"end")
            is_answer = False
        num_entry.insert("end",value)
 
def math_press(value):
    global op 
    global temp_num
    global is_answer
    if not num_entry.get() == '':
        op = value
        temp_num = int(num_entry.get())
        num_entry.delete(0,'end')
 
def equal_press():
    global op
    global temp_num
    global is_answer
    if not (op =='' and num_entry.get()==''):
        num = int(num_entry.get())
        if op == '*':
            solution = temp_num*num
        elif op == '+':
            solution = temp_num+num
        else :
            solution = temp_num-num
        num_entry.delete(0,'end')
        num_entry.insert(0,solution)
        op = ''
        temp_num = 0
        is_answer = True
         
     
root = Tk()
root.title("Calculator")
root.geometry("320x200")
 
entry_value = StringVar(root, value='')
 
num_entry = ttk.Entry(root, textvariable = entry_value, width=20)
button7 = ttk.Button(root, text="7", command = lambda:press('7'))
button8 = ttk.Button(root, text="8", command = lambda:press('8'))
button9 = ttk.Button(root, text="9", command = lambda:press('9'))
button4 = ttk.Button(root, text="4", command = lambda:press('4'))
button5 = ttk.Button(root, text="5", command = lambda:press('5'))
button6 = ttk.Button(root, text="6", command = lambda:press('6'))
button1 = ttk.Button(root, text="1", command = lambda:press('1'))
button2 = ttk.Button(root, text="2", command = lambda:press('2'))
button3 = ttk.Button(root, text="3", command = lambda:press('3'))
button0 = ttk.Button(root, text="0", command = lambda:press('0'))
button_mult = ttk.Button(root, text="*", command = lambda:math_press('*'))
button_c = ttk.Button(root, text="C", command = lambda:press('C'))
button_add = ttk.Button(root, text="+", command = lambda:math_press('+'))
button_sub = ttk.Button(root, text="-", command = lambda:math_press('-'))
button_equal = ttk.Button(root, text="=", command = lambda:equal_press())

# grid
num_entry.grid(row=0, columnspan=3) 
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button0.grid(row=4, column=0)
button_mult.grid(row=4, column=1)
button_c.grid(row=4, column=2)
button_add.grid(row=5, column=0)
button_sub.grid(row=5, column=1)
button_equal.grid(row=5, column=2)

root.mainloop()