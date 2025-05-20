from tkinter import *
from pynput import keyboard
import pyautogui
import time
def main():
    text1 = entry.get()
    if text1:
        time.sleep(1)
        pyautogui.write(text1, interval=0.02)


def on_press(key):
    try:
        if key == keyboard.Key.f6:  
            main()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()


window = Tk()
window.geometry("900x400")
window.title("Wpm Bot")
window.config(bg="#00ff00")

label1 = Label(window, bg="#00ff00", text="Welcome to Wpm Bot..", font=("Impact", 35)).grid(column=0, row=0)
label2 = Label(window, bg="#00ff00", font=("Impact", 30), text="Enter your text here: ").grid(column=0, row=1)
entry = Entry(window, font=("Impact", 25), fg="#00ff00", bg="black")
entry.grid(column=1, row=1)
label3 = Label(window, text="Press F6 to start.", font=("Impact", 30), fg="black", bg="#00ff00").grid(column=0, row=2, columnspan=2)

window.mainloop()
