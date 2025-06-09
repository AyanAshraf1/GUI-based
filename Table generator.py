from tkinter import *
from tkinter import messagebox

def main():
    global text_label
    global answer
    try:
        user = int(entry.get())
        text_label = ""
        for i in range(1, 11):
            t = i * user
            text_label += f"{user}*{i} = {t}\n"
        label.config(text=text_label)
    except ValueError:
        messagebox.showerror(title="error", message="Please enter a valid number.")

window = Tk()
answer = IntVar()
text_label = ""
green = "#00ff00"
window.title("Table generator")
window.config(bg=green)
window.resizable(False, False)
entry = Entry(window, font=("consolas", 30))
entry.grid(column=0, row=0)
Button(window, font=("Impact", 35), text="Generate", command=main,
       fg="blue", bg="red", activebackground="blue", activeforeground="red").grid(column=0, row=1, columnspan=2)
label = Label(window, font=("Impact", 38), bg=green, text=text_label)
label.grid(column=0, row=2)
window.mainloop()
