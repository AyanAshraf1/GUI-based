from tkinter import *
from tkinter import messagebox

def button_press(num):
    global equation_text
    global equation_label
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
    except ZeroDivisionError:
        messagebox.showerror(title="error",message="Can't divide a number by zero")
        equation_text = ""
        equation_label.set(equation_text)
    except SyntaxError:
        messagebox.showerror(title="error", message="Syntax Error")
        equation_text = ""
        equation_label.set(equation_text)  

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.title("Calculator")
window.resizable(False,False)
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=("consolas", 23), bg="white", width=24,
              height=2)

label.pack()
frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35, command= lambda:button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,font=35, command= lambda:button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,font=35, command= lambda:button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35, command= lambda:button_press(4))
button4.grid(row=0,column=3)

button5 = Button(frame,text=5,height=4,width=9,font=35, command= lambda:button_press(5))
button5.grid(row=1,column=0)

button6 = Button(frame,text=6,height=4,width=9,font=35, command= lambda:button_press(6))
button6.grid(row=1,column=1)

button7 = Button(frame,text=7,height=4,width=9,font=35, command= lambda:button_press(7))
button7.grid(row=1,column=2)

button8 = Button(frame,text=8,height=4,width=9,font=35, command= lambda:button_press(8))
button8.grid(row=1,column=3)

button9 = Button(frame,text=9,height=4,width=9,font=35, command= lambda:button_press(9))
button9.grid(row=2,column=0)

button0 = Button(frame,text=0,height=4,width=9,font=35, command= lambda:button_press(0))
button0.grid(row=2,column=1)

plus = Button(frame,text="+",height=4,width=9,font=35, command= lambda:button_press('+'))
plus.grid(row=0,column=4)

minus = Button(frame,text="-",height=4,width=9,font=35, command= lambda:button_press('-'))
minus.grid(row=1,column=4)

multiply = Button(frame,text="*",height=4,width=9,font=35, command= lambda:button_press('*'))
multiply.grid(row=2,column=4)

divide = Button(frame,text="/",height=4,width=9,font=35, command= lambda:button_press('/'))
divide.grid(row=2,column=3)

equals = Button(frame,text="=",height=4,width=9,font=35, command= equals)
equals.grid(row=2,column=2)

decimal = Button(frame,text=".",height=4,width=9,font=38, command= lambda:button_press('.'))
decimal.grid(row=3,column=0)

clear = Button(frame,text="clear",height=4,width=9,font=35, command= clear)
clear.grid(row=3,column=1)
window.mainloop()
