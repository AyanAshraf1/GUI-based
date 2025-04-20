from tkinter import *
i = ""
def main():
    global i
    var = int(scale.get())
    if var <= 50:
        i = "Good"
        label.config(text=i, fg="#00FF00")
    elif var >= 51 and var <= 99:
        i = "Moderate"
        label.config(text=i, fg="yellow")
    elif var >= 100 and var <= 149:
        i = "Unhealthy for sensitive groups"
        label.config(text=i, fg="orange")
    elif var >= 150 and var <= 199:
        i = "Unhealthy"
        label.config(text=i, fg="red")
    elif var >= 200 and var <= 299:
        i = "Very unhealthy"
        label.config(text=i, fg="purple")
    elif var >= 300:
        i = "Hazardous"
        label.config(text=i, fg="maroon")




window = Tk()
window.title("AQI index")
scale = Scale(window, from_=0, to=500,  length=300, troughcolor='#69EAFF',
              fg = '#FF1C00')
window.config(bg="#002B5B")
window.resizable(False,False)
button = Button(window, text="Check", font=("Impact", 32), command=main, fg="#00FF00", bg="black",
                activebackground="black", activeforeground="#00FF00")
scale.pack()
button.pack()
label = Label(window, font=("Impact", 30), text=i, bg="#002B5B")
label.pack()
window.mainloop()
