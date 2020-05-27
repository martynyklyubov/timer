
from tkinter import *
import time
import subprocess

global COUNT 
COUNT = 20

fen = Tk()
fen.title("COUNTDOWN")
canv = Canvas(fen, height=100, width=300, bg="green")
canv.grid(row=0, column=0, rowspan=3, padx=8, pady=8)
lab = Label(fen, text="Press Start", fg="black", bg="orange", font=("Impact", 30))
lab.grid(row=0, column=0)

TIME = 1500
CLOCKING = None

def start(ltime):
    global TIME
    global CLOCKING
    mins, secs = divmod(ltime, 60)
    timer ='{:02d}:{:02d}'.format(mins, secs)
    if (ltime == 0):
        subprocess.call(["afplay", "woohoo.wav"])
        lab.config(text="STOP", fg="black", bg="orange", font=("Impact", 18))
    elif (ltime > 0):
        lab.config(text=timer, font=("Impact", 30))
        TIME = ltime - 1
        CLOCKING = fen.after(1000, start, TIME)

lab = Label(fen, text="", fg="black", bg="red", font=("Impact", 18))
lab.grid(row=2, column=0)


def pause():
    global CLOCKING
    global TIME
    if CLOCKING != None:
        fen.after_cancel(CLOCKING)
    
def reset():
    global TIME
    global CLOCKING
    if CLOCKING != None:
        fen.after_cancel(CLOCKING)
    TIME = 1500
    mins, secs = divmod(TIME, 60)
    timer ='{:02d}:{:02d}'.format(mins, secs)
    lab.config(text=timer, font=("Impact", 30))


Countdown1 = Button(fen, text="START", command=lambda: start(TIME), fg="black", bg="orange", font=("Impact", 18))
Countdown1.grid(row=0, column=1, sticky = E)
Countdown2 = Button(fen, text="PAUSE", command=pause, fg="black", bg="orange", font=("Impact", 18))
Countdown2.grid(row=1, column=1, sticky = E)
Countdown3 = Button(fen, text="RESET", command=reset, fg="black", bg="orange", font=("Impact", 18))
Countdown3.grid(row=2, column=1, sticky = E)

fen.mainloop()