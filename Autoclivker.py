from tkinter import *
import pyautogui
from pynput import keyboard
import time
import threading

clicking = False
desired_cps = 12345678930
sleep_time = 1 / desired_cps

def main():
    global clicking
    while clicking:
        pyautogui.click()
        time.sleep(sleep_time)

def on_press(key):
    global clicking
    try:
        if key == keyboard.Key.f6:  
            clicking = True
            threading.Thread(target=main, daemon=True).start()
        elif key == keyboard.Key.f8:
            clicking = False
            window.destroy()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

window = Tk()
window.title("Autoclicker")
window.config(bg="#00ff00")
window.geometry("680x480")
label = Label(window, text="Press F6 to start and F8 to stop.", font=("Impact", 40), bg="#00ff00")
label.pack(side=TOP)

window.mainloop()

listener.stop()

