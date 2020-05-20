
from tkinter import *
import time

fen = Tk()
fen.title("COUNTDOWN")

canv = Canvas(fen, height=100, width=200, bg="orange")
canv.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

def start(t=25):
    global i
    i = 1
    if (i == 1):
        lab.config(text=str(t), font=("Impact", 18))
        if (t>0):
            fen.after(1000, start, t-1)
    else:
        i = 1
        lab.config(text="stop", fg="black", bg="orange", font=("Impact", 18))

lab = Label(fen, text="", fg="black", bg="orange", font=("Impact", 18))
lab.grid(row=0, column=0)

Countdown = Button(fen, text="START", command=start, fg="black", bg="orange", font=("Impact", 18))
Countdown.grid(row=1, column=0)

fen.mainloop()

"""
different method
"""
# import tkinter as tk
# import time as tm

# def display_time():
#     current_time = tm.strftime('%H:%M:%S')
#     clock_label['text'] = current_time
#     root.after(1000, display_time)

# root = tk.Tk()
# root.title('Digital Clock')
# clock_label = tk.Label(root,font='ariel 100', bg="orange", fg="black")
# button = tk.Button(root, text='START')
# button.pack()
# clock_label.grid(row=0,column=0)
# display_time()
# root.mainloop() 
