from tkinter import *
i = ""

def main():
    global i
    var = str(list.get(list.curselection()))
    i = (f"here is your {var}")
    label.config(text=i)
def pain():
    list.insert(list.size(),entry.get())
    list.config(height=list.size())
def delete():
    list.delete(list.curselection())
    list.config(height=list.size())



window = Tk()
window.title("Food shop")
list = Listbox(window, bg="#f7ffde",
               font=("Constantia", 32),
               width=15
               )
window.config(bg="orange")
window.resizable(False,False)
list.pack()
list.insert(1, "pizza")
list.insert(2, "shawarma")
list.insert(3, "biryani")
list.insert(4, "butter chicken")
list.config(height=list.size())
entry = Entry(window, font=("Impact", 30))
entry.pack()
submit = Button(window, text="Submit", command=main, font=("Impact", 40),
                bg="black",activebackground="black",
                fg="#00FF00",activeforeground="#00FF00")
add = Button(window, text="add", command=pain, font=("Impact", 40),
                bg="black",activebackground="black",
                fg="#00FF00",activeforeground="#00FF00")
delete  = Button(window, text="delete", command=delete, font=("Impact", 40),
                bg="black",activebackground="black",
                fg="#00FF00",activeforeground="#00FF00")
add.pack()
delete.pack()
submit.pack(side=BOTTOM)
label = Label(window, text=i, font =("Arial", 40), bg="orange")
label.pack(side=BOTTOM)
window.mainloop()
