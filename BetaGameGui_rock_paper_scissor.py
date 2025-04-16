from tkinter import *
import random
import time

def main(player_choice):
    choices = ['rock', 'paper', 'scissors']
    bot = random.choice(choices)

    p1 = player_choice
    print(f"Player: {p1}, Bot: {bot}")
    if player_choice == bot:
        print("Tie")
    elif player_choice == "rock" and bot == "scissors":
        print("You won")
    elif player_choice == "paper" and bot == "rock":
        print("You won")
    elif player_choice == "scissors" and bot == "paper":
        print("You won")
    else:
        print("You lost")

window = Tk()

button1 = Button(window,
                 fg="#00FF00",
                 font=30,
                 background="black",
                 text="Rock",
                 command=lambda: main("rock"))
button2 = Button(window,
                 fg="#00FF00",
                 font=30,
                 background="black",
                 text="Paper",
                 command=lambda: main("paper"))
button3 = Button(window,
                 fg="#00FF00",
                 font=30,
                 background="black",
                 text="Scissors",
                 command=lambda: main("scissors"))

window.title("Rock, Paper, Scissors Game")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
window.geometry("240x240")

window.mainloop()
