import time
import webbrowser
from tkinter import *
def main():
    url = entry_url.get()
    duration = int(entry_dur.get())
    views = int(entry.get())
    for i in range(0, views):
        webbrowser.open(url)
        time.sleep(duration)

window = Tk()
label = Label(window,
              text="Yt view bot...",
              font=("Arial",40),
              fg="#00FF00",
              bg="black")
window.config(background="black")
window.title("Yt view bot")
label.place(x=300,y=0)
label2= Label(window,
              text="Number of views: ",
              font=("Arial", 30),
              fg="#00FF00",
              bg="black"
              )
label2.place(x=50,y=250)
entry = Entry(window,

              font=("Arial",30),
              fg="#00FF00")
entry.place(x=350,y=250)
labelurl = Label(window,
              text="Url/link: ",
              font=("Arial", 30),
              fg="#00FF00",
              bg="black"
              )
entry_url = Entry(window,

              font=("Arial",30),
              fg="#00FF00")
entry_url.place(x=350,y=310)
labelurl.place(x=50,y=310)
labelvid = Label(window,
              text="Video duration: ",
              font=("Arial", 30),
              fg="#00FF00",
              bg="black"
              )
labelvid.place(x=50,y=369)
entry_dur = Entry(window,

              font=("Arial",30),
              fg="#00FF00")
entry_dur.place(x=350,y=369)
label_secs = Label(window,
              text="seconds",
              font=("Arial", 30),
              fg="#00FF00",
              bg="black"
              )
label_secs.place(x=793,y=369)
Go = Button(window,
            text="Go",
            font=50,
            fg="red",

            command=main)
Go.place(x=450,y=469)
window.mainloop()
