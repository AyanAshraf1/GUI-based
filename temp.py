from tkinter import *
i = ""
def submit():
    global i
    var = int(scale.get())
    i = var
    if i <= 20:
        label.config(text=f"{i} celsius",fg = "#69EAFF")
    elif i >= 40 and i <60:
        label.config(text=f"{i} celsius", fg="red")
    elif i >= 60:
        label.config(text=f"{i} celsius", fg="#8B0000")

    else:
        label.config(text=f"{i} celsius", fg="#FFA500")
window = Tk()
window.resizable(False, False)
scale = Scale(window, from_= 0, to=100, length=300, tickinterval=10,
              troughcolor='#69EAFF',
              fg = '#FF1C00')
window.config(bg="#002B5B")
scale.pack()
button = Button(window, text="submit",font=("Impact",30),command=submit, fg="#00FF00", bg="black",
                activebackground="black",
                activeforeground="#00FF00")
label = Label(window, text=i, font=("Impact", 30))
label.pack(side=BOTTOM)
window.title("Temperature changer")
button.pack()
window.mainloop()
