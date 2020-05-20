
from tkinter import *
import time

fen = Tk()
fen.title("COUNTDOWN")
canv = Canvas(fen, height=100, width=200, bg="orange")
canv.grid(row=0, column=0, rowspan=3, padx=8, pady=8)

global i
i = 0

# def restart():


def start(t=5):

    i = 1
    if (i == 1):
        lab.config(text=str(t), font=("Impact", 30))
        if (t>0):
            fen.after(1000, start, t-1)
    else:
        i = 1
        lab.config(text="stop", fg="black", bg="orange", font=("Impact", 18))
lab = Label(fen, text="", fg="black", bg="orange", font=("Impact", 18))
lab.grid(row=1, column=0)

def stop(t):
    global i
    i = t

Countdown1 = Button(fen, text="START", command=start, fg="black", bg="orange", font=("Impact", 18))
Countdown1.grid(row=0, column=1, sticky = E)
Countdown2 = Button(fen, text="STOP", command=stop, fg="black", bg="orange", font=("Impact", 18))
Countdown2.grid(row=1, column=1, sticky = E)
Countdown3 = Button(fen, text="RESET", command=stop, fg="black", bg="orange", font=("Impact", 18))
Countdown3.grid(row=2, column=1, sticky = E)

fen.mainloop()
