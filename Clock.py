from tkinter import *
from time import *
def update():
    timestr = strftime("%I:%M:%S %p")
    time_label.config(text=timestr)
    
    day_str = strftime("%A")
    day_label.config(text=day_str)
    date_str = strftime("%B %d, %Y")
    date_label.config(text=date_str)
    window.after(1000,update)
    
window = Tk()
time_label = Label(window, font=("Impact", 50), fg="#00ff00", bg="black")
time_label.pack()
day_label = Label(window, font=("Ink Free", 26))
day_label.pack()
date_label = Label(window, font=("Ink Free", 34))
date_label.pack()
window.geometry("420x420")
update()
window.title("Clock program")

window.mainloop()
