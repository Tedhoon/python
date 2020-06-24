from tkinter import *
from tkinter import ttk

class Frame():

    def __init__(self):
        self.op = ''  
        self.temp_num = 0
        self.is_answer = False

        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("320x200")

        self.entry_value = StringVar(self.root, value='')

        self.num_entry = ttk.Entry(self.root, textvariable = self.entry_value, width=20)
        self.button7 = ttk.Button(self.root, text="7", command = lambda:self.press('7'))
        self.button8 = ttk.Button(self.root, text="8", command = lambda:self.press('8'))
        self.button9 = ttk.Button(self.root, text="9", command = lambda:self.press('9'))
        self.button4 = ttk.Button(self.root, text="4", command = lambda:self.press('4'))
        self.button5 = ttk.Button(self.root, text="5", command = lambda:self.press('5'))
        self.button6 = ttk.Button(self.root, text="6", command = lambda:self.press('6'))
        self.button1 = ttk.Button(self.root, text="1", command = lambda:self.press('1'))
        self.button2 = ttk.Button(self.root, text="2", command = lambda:self.press('2'))
        self.button3 = ttk.Button(self.root, text="3", command = lambda:self.press('3'))
        self.button0 = ttk.Button(self.root, text="0", command = lambda:self.press('0'))
        self.button_mult = ttk.Button(self.root, text="*", command = lambda:self.math_press('*'))
        self.button_c = ttk.Button(self.root, text="C", command = lambda:self.press('C'))
        self.button_add = ttk.Button(self.root, text="+", command = lambda:self.math_press('+'))
        self.button_sub = ttk.Button(self.root, text="-", command = lambda:self.math_press('-'))
        self.button_equal = ttk.Button(self.root, text="=", command = lambda:self.equal_press())
        

    def get_frame(self):
        # grid
        self.num_entry.grid(row=0, columnspan=3) 
        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)
        self.button0.grid(row=4, column=0)
        self.button_mult.grid(row=4, column=1)
        self.button_c.grid(row=4, column=2)
        self.button_add.grid(row=5, column=0)
        self.button_sub.grid(row=5, column=1)
        self.button_equal.grid(row=5, column=2)
        self.root.mainloop()

        
    def press(self, value):
        if value=='C':
            self.num_entry.delete(0,'end')
            self.op = ''
            self.is_answer = False
        else:
            if self.is_answer:
                self.num_entry.delete(0,"end")
                self.is_answer = False
            self.num_entry.insert("end",value)
    
    def math_press(self, value):
        if not self.num_entry.get() == '':
            self.op = value
            self.temp_num = int(self.num_entry.get())
            self.num_entry.delete(0,'end')
    
    def equal_press(self):
        if not (self.op =='' and self.num_entry.get()==''):
            num = int(self.num_entry.get())
            if self.op == '*':
                solution = self.temp_num*num
            elif self.op == '+':
                solution = self.temp_num+num
            else :
                solution = self.temp_num-num
            self.num_entry.delete(0,'end')
            self.num_entry.insert(0,solution)
            self.op = ''
            self.temp_num = 0
            self.is_answer = True
            print(solution)


class Calculator(Frame):

    def __init__(self):
        super().__init__()
        self.get_frame()


if __name__ == "__main__":
    cal = Calculator()
    cal
