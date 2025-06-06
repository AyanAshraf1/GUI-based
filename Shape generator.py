from tkinter import *
import turtle
import time

turt = turtle.Turtle()
display = turtle.Screen()
display.title("Shape generator")
turt.shape("turtle")
def square():
    
    window.destroy()
    turt.showturtle()
    turt.begin_fill()
    for i in range(1,5):
        turt.forward(150)
        turt.left(90)
    turt.fillcolor("#00ff00")
    turt.end_fill()
    
def circle():
    
    window.destroy()
    turt.showturtle()
    turt.begin_fill()
    turt.circle(125,360,25)
    turt.fillcolor("blue")
    turt.end_fill()
    

def rectangle():
    
    window.destroy()
    turt.showturtle()
    time.sleep(0.1)
    for i in range(0,2):
        turt.speed(10)
        turt.begin_fill()
        turt.forward(150)
        turt.left(90)
        turt.speed(0)
        turt.forward(200)
        turt.left(90)
        turt.fillcolor("purple")
        turt.end_fill()
    
def triangle():
    
    window.destroy()
    turt.showturtle()
    time.sleep(0.1)
    for i in range(0,2):
        turt.speed(10)
        turt.begin_fill()
        turt.forward(150)
        turt.left(90)
        turt.fillcolor("orange")
    turt.setheading(-135)
    turt.forward(212.13)
    turt.end_fill()
    
def heart():
    window.destroy()
    turt.showturtle()
    time.sleep(0.1)
    turt.speed(10)
    turt.begin_fill()
    turt.left(140)
    turt.forward(180)
    turt.circle(-90,200)
    turt.setheading(60)
    turt.circle(-90,200)
    turt.forward(180)
    turt.fillcolor("red")
    turt.end_fill()
    
    

window = Tk()
window.title("shape generator")
window.geometry("500x600")
window.config(bg="black")
window.resizable(False,False)
Button(window, text=" Square ", command=square,font=("Impact",40),fg="#00ff00",bg="blue",
       activebackground="#00ff00", activeforeground="blue").grid(column=3,row=0)
Button(window, text="rectange", command=rectangle,font=("Impact",40),fg="#00ff00",bg="blue",
       activebackground="#00ff00", activeforeground="blue").grid(column=3,row=1)
Button(window, text="circle ", command=circle,font=("Impact",40),fg="#00ff00",bg="blue",
       activebackground="#00ff00", activeforeground="blue").grid(column=3,row=2)
Button(window, text="triangle", command=triangle,font=("Impact",40),fg="#00ff00",bg="blue",
       activebackground="#00ff00", activeforeground="blue").grid(column=3,row=3)
Button(window, text=" heart ", command=heart,font=("Impact",40),fg="#00ff00",bg="blue",
       activebackground="#00ff00", activeforeground="blue").grid(column=3,row=4)
window.mainloop()
display.mainloop()
