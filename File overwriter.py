from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
warn = False
def file():
    global f
    f = f = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("HTML Files", "*.html")])
def main():
    try:
        global warn
        global f
        inp = entry.get()
        warn = messagebox.askokcancel(title="Warning",message="This action will delete the previous data and it is not possible to undo it.")
        if warn:
            with open(str(f),'w') as File:
              File.write(inp)
    except NameError:
        messagebox.showerror(title="error", message="Error please choose a file first..")

window = Tk()
window.resizable(False,False)
window.title("File overwriter")
window.config(bg="#00ff00")
entry = Entry(window, font=("Impact", 30))
entry.grid(column=0,row=0)
Button(window, command=main, text="copy", font=("Impact",40), fg="green", bg="black",
       activebackground="orange", activeforeground="blue"
       ).grid(column=0,row=1,columnspan=3)
Button(window, command=file, text="open", font=("Impact",40), fg="green", bg="black",
       activebackground="orange", activeforeground="blue"
       ).grid(column=0,row=2,columnspan=3)
window.mainloop()
