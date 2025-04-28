from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import time

def main():
    choos = messagebox.askyesno(title="Question", message="Is ronaldo good?")
    print(choos)
    if choos:
        window.config(background="#00FF00")
    else:
        window.config(background="red")
        while True:
            messagebox.showerror(title="Punishment",message="Get tortured")



window = Tk()
button=Button(window, command=main, text="press me", font=("Impact", 50), fg="#00FF00", activeforeground="#00FF00",
              bg="black",activebackground="black")
window.geometry("320x320")
window.resizable(False,False)
window.title("Q/A")
button.pack()
window.mainloop()


