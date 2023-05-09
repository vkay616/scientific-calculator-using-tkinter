from math import *
from tkinter import *
from tkinter import messagebox
from typing import Counter


class Calculator:

    def __init__(self, root):
        self.root = root

        self.counter = 0

        # DISPLAY FRAME
        self.display_frame = LabelFrame(self.root, bg='#000000', font=('helvetica', 10), bd=0)
        self.display_frame.place(x=0, y=0, width=358, height=60)

        # DISPLAY ENTRY
        self.limiter = StringVar()
        self.display_limit(self.limiter)

        self.display = Entry(self.display_frame, bd=0, font=('helvetica', 14, 'bold'), justify='right', borderwidth=0, relief=FLAT, textvariable=self.limiter)
        self.display.bind("<Key>", lambda e: "break")
        self.display.place(x=0, y=0, width=358, height=60)

        # BUTTON FRAME
        self.button_frame = LabelFrame(self.root, bg='#000000', font=('helvetica', 10), bd=0, relief=FLAT)
        self.button_frame.place(x=4, y=60, width=350, height = 395)

        # BUTTON PLACEMENTS
        Button(self.button_frame, text="π", command= self.pi, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=0, column=0, padx=(4,4), pady=(10, 4))
        Button(self.button_frame, text="e", command= self.e, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=0, column=1, padx=4, pady=(10, 4))
        Button(self.button_frame, text="|x|", command= self.mod, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=0, column=2, padx=4, pady=(10, 4))
        Button(self.button_frame, text="AC", command= self.ac, bg="#b62d12", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=0, column=3, padx=4, pady=(10, 4))
        Button(self.button_frame, text="DEL", command= self.delete, bg="#b62d12", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=0, column=4, padx=4, pady=(10, 4))

        Button(self.button_frame, text="^2", command= self.square, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=1, column=0, padx=(4,4), pady=4)
        Button(self.button_frame, text="sqrt", command= self.sqrt, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=1, column=1, padx=4, pady=4)
        Button(self.button_frame, text="ln", command= self.ln, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=1, column=2, padx=4, pady=4)
        Button(self.button_frame, text="x!", command= self.factorial, bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=1, column=3, padx=4, pady=4)
        Button(self.button_frame, text="/", command= lambda :self.get_input('/'), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=1, column=4, padx=4, pady=4)

        Button(self.button_frame, text="sin", command= lambda :self.get_input('sin('), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=2, column=0, padx=(4,4), pady=4)
        Button(self.button_frame, text="7", command= lambda :self.get_input('7'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=2, column=1, padx=4, pady=4)
        Button(self.button_frame, text="8", command= lambda :self.get_input('8'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=2, column=2, padx=4, pady=4)
        Button(self.button_frame, text="9", command= lambda :self.get_input('9'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=2, column=3, padx=4, pady=4)
        Button(self.button_frame, text="*", command= lambda :self.get_input('*'), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=2, column=4, padx=4, pady=4)

        Button(self.button_frame, text="cos", command= lambda :self.get_input('cos('), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=3, column=0, padx=(4,4), pady=4)
        Button(self.button_frame, text="4", command= lambda :self.get_input('4'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=3, column=1, padx=4, pady=4)
        Button(self.button_frame, text="5", command= lambda :self.get_input('5'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=3, column=2, padx=4, pady=4)
        Button(self.button_frame, text="6", command= lambda :self.get_input('6'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=3, column=3, padx=4, pady=4)
        Button(self.button_frame, text="+", command= lambda :self.get_input('+'), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=3, column=4, padx=4, pady=4)

        Button(self.button_frame, text="tan", command= lambda :self.get_input('tan('), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=4, column=0, padx=(4,4), pady=4)
        Button(self.button_frame, text="1", command= lambda :self.get_input('1'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=4, column=1, padx=4, pady=4)
        Button(self.button_frame, text="2", command= lambda :self.get_input('2'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=4, column=2, padx=4, pady=4)
        Button(self.button_frame, text="3", command= lambda :self.get_input('3'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=4, column=3, padx=4, pady=4)
        Button(self.button_frame, text="-", command= lambda :self.get_input('-'), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=4, column=4, padx=4, pady=4)

        Button(self.button_frame, text="(", command= lambda :self.get_input('('), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=5, column=0, padx=(4,4), pady=4)
        Button(self.button_frame, text=")", command= lambda :self.get_input(')'), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=5, column=1, padx=4, pady=4)
        Button(self.button_frame, text="0", command= lambda :self.get_input('0'), bg="#2d3436", fg="#c1bb10", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=5, column=2, padx=4, pady=4)
        Button(self.button_frame, text=".", command= lambda :self.get_input('.'), bg="#2d3436", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=5, column=3, padx=4, pady=4)
        Button(self.button_frame, text="=", command= self.solve, bg="#c1bb10", fg="#ffffff", bd=0, font=("helvetica", 10, 'bold'), width=7, height=3).grid(row=5, column=4, padx=4, pady=4)

    # FUNCTION TO LIMIT THE NUMBER OF CHARACTERS DISPLAYED ON THE SCREEN
    def display_limit(self, str_var):
        def callback(str_var):
            counter = str_var.get()[:32]
            str_var.set(counter)
        
        str_var.trace("w", lambda name, index, mode, str_var=str_var: callback(str_var))
    
    # BUTTON FUNCTIONS 

    # AC BUTTON
    def ac(self):
        self.display.delete(0, END)
        self.counter = 0
    
    # DELETE BUTTON
    def delete(self):
        self.expression = self.display.get()
        self.new_expression = self.expression[:-1]
        self.ac()
        self.display.insert(0, self.new_expression)
        self.counter -= 1
    
    # GETTING INPUT FROM BUTTONS
    def get_input(self, input_button):
        self.length = len(input_button)
        self.display.insert(self.counter, input_button)
        self.counter += self.length
        
        if self.counter > 32:
            messagebox.showwarning(title='Warning', message='Maximum 32 characters allowed!')
            self.ac()

    # EQUALS BUTTON
    def solve(self):
        self.expression = self.display.get()
        try:
            self.result = eval(self.expression)
            self.ac()
            self.display.insert(0, self.result)
            self.counter = len(str(self.result))

        except Exception as e:
            #messagebox.showerror(title='Error', message='Something went wrong. Please try again later!')
            messagebox.showerror('error is', e)
            self.ac()

    # PI BUTTON
    def pi(self):
        self.expression = self.display.get()
        try:
            self.new_expression = self.expression + "*3.14"
            self.result = eval(self.new_expression)
            self.ac()
            self.display.insert(0, self.result)
        except Exception:
            messagebox.showerror(title="Error", message="Something went wrong. Please try again later!")
            self.ac()

    # E BUTTON
    def e(self):
        self.expression = self.display.get()
        try:
            self.new_expression = self.expression + "*2.718"
            self.result = eval(self.new_expression)
            self.ac()
            self.display.insert(0, self.result)
        except Exception:
            messagebox.showerror(title="Error", message="Something went wrong. Please try again later!")
            self.ac()
    
    # MOD BUTTON
    def mod(self):
        self.expression = self.display.get()
        try:
            self.ac()
            if "." in self.expression:
                self.result = abs(float(self.expression))
            else:
                self.result = abs(int(self.expression))
            
            self.display.insert(0, self.result)
        except Exception:
            messagebox.showerror(title="Error", message="Something went wrong. Please try again later!")
            self.ac()

    # SQUARE BUTTON
    def square(self):
        self.expression = self.display.get()
        try:
            self.new_expression = self.expression + "**2"
            self.result = eval(self.new_expression)
            self.ac()
            self.display.insert(0, self.result)
        except Exception:
            messagebox.showerror(title="Error", message="Something went wrong. Please try again later!")
            self.ac()

    # SQUARE ROOT BUTTON
    def sqrt(self):
        self.expression = self.display.get()
        try:
            self.new_expression = self.expression + "**0.5"
            self.result = eval(self.new_expression)
            self.ac()
            self.display.insert(0, self.result)
        except Exception:
            messagebox.showerror(title="Error", message="Something went wrong. Please try again later!")
            self.ac()
    
    # LN BUTTON
    def ln(self):
        self.expression = self.display.get()
        try:
            self.result = log(float(self.expression))
            self.ac()
            self.display.insert(0, self.result)
        except Exception:
            messagebox.showerror(title="Error", message="Something went wrong. Please try again later!")
            self.ac()
    
    # FACTORIAL BUTTON
    def factorial(self):
        self.expression = self.display.get()
        try:
            self.result = factorial(int(self.expression))
            self.ac()
            self.display.insert(0, self.result)
        except Exception:
            messagebox.showerror(title="Error", message="Something went wrong. Please try again later!")
            self.ac()
    

root = Tk()
root.title('Calculator')
root.geometry('358x455')
root.resizable(0, 0)
root.configure(bg='#000000')
root.iconbitmap(r'<YOUR FILE DIRECTORY FOR THE ICON IMAGE>')

Calculator(root)

root.mainloop()