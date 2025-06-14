from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        global planets
        mass = float(mass_entry.get())
        p = planet_entry.get().replace(" ", "")
        planet = p.lower()
    
        g = planets.get(planet)  
    
        if g is None:  
           messagebox.showerror("Error", "Invalid planet name!")
           return

        answer = f"{g * mass} KN"
        label.config(text=answer)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
    
planets = {
    "earth" : 9.8,
    "mars":  3.7,
    "mercury": 3.7,
    "venus": 8.9,
    "jupiter": 24.7,
    "saturn": 9.0,
    "uranus": 8.7,
    "neptune": 11,
    "sun": 274
}
window = Tk()
window.config(bg="#00ff00")
window.geometry("1300x700")
mass_label = Label(window,text="Enter your mass in KG: ", font=("Impact", 38), bg="#00ff00").grid(column=0,row=0)
mass_entry = Entry(window, font=("Impact", 32))
mass_entry.grid(column=1,row=0)
planet_label = Label(window, text="Enter your planet you are living on: ", font=("Impact", 38), bg="#00ff00").grid(column=0,row=1)
planet_entry = Entry(window, font=("Impact", 32))
planet_entry.grid(column=1,row=1)
Button(window, text="Calculate", font=("consolas", 40), bg="red", fg="blue", activebackground="blue", activeforeground="red", command=calculate).grid(column=0,row=2,columnspan=2)
window.title("Weight Calculator")
label = Label(window, font=("Impact", 38),bg="#00ff00")
label.grid(column=0,row=3,columnspan=3)
window.mainloop()
