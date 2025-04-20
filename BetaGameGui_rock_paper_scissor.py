from tkinter import *
import random
import time
i =""
x=""
def main(player_choice):
    global i
    global x
    choices = ['rock', 'paper', 'scissors']
    bot = random.choice(choices)

    p1 = player_choice
    x = (f"you: {p1}, bot={bot}")
    label2.config(text=x)

    if player_choice == bot:
        i = "tie"
        label.config(text=i,fg="red")
    elif player_choice == "rock" and bot == "scissors":
        i = "You won"
        label.config(text=i, fg="green")
    elif player_choice == "paper" and bot == "rock":
        i = "You won"
        label.config(text=i, fg="green")
    elif player_choice == "scissors" and bot == "paper":
        i = "You won"
        label.config(text=i, fg="green")
    else:
        i = "You lost"
        label.config(text=i, fg="red")

window = Tk()

button1 = Button(window,
                 fg="#00FF00",
                 font=("Impact", 69),
                 background="black",
                 text="Rock",
                 command=lambda: main("rock"))
button2 = Button(window,
                 fg="#00FF00",
                 font=("Impact", 69),
                 background="black",
                 text="Paper",
                 command=lambda: main("paper"))
button3 = Button(window,
                 fg="#00FF00",
                 font=("Impact", 69),
                 background="black",
                 text="Scissors",
                 command=lambda: main("scissors"))

window.title("Rock, Paper, Scissors Game")
button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=TOP)
label = Label(window, text=i, font=("Impact", 50))
label.pack(side=BOTTOM)
label2 = Label(window, text=x, font=("Impact", 50))
label2.pack(side=BOTTOM)
window.geometry("720x720")

window.mainloop()
