from tkinter import *
i = ""
mcqs = ["...", "5", "4", "911"]

def main():
    global i
    if (x.get()==2):
        i = "Correct"
        label2.config(text=i, fg="green")
        
    else:
        
        i = "wrong"
        label2.config(text=i, fg="red")

window = Tk()
x = IntVar()
window.title("Mcq test")
label1 = Label(window, text="What is 2+2?", font=("Impact", 55))
label2 = Label(window, text=i, font=("Impact", 30))
label2.pack(side=BOTTOM)
label1.pack(side=TOP)
for index in range(len(mcqs)):
    radioactive = Radiobutton(window,text=mcqs[index], font=("Arial",42), variable=x,value=index)
    radioactive.pack(anchor=W)
submit = Button(window, text="Submit", font=("Impact", 30), command=main)
submit.pack()
window.mainloop()
