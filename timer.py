
from tkinter import *
import time
import subprocess



global COUNT 
COUNT = 20

fen = Tk()
fen.title("COUNTDOWN")
canv = Canvas(fen, height=100, width=200, bg="orange")
canv.grid(row=0, column=0, rowspan=3, padx=8, pady=8)
lab = Label(fen, text="", fg="black", bg="orange", font=("Impact", 18))
lab.grid(row=1, column=0)

TIME = 10
CLOCKING = None

def start(ltime):
    global TIME
    global CLOCKING
    print("This is global time" + str(TIME))
    print("This is local start time" + str(ltime))
    mins, secs = divmod(ltime, 60)
    timer ='{:02d}:{:02d}'.format(mins, secs)
    if (ltime == 0):
        subprocess.call(["afplay", "woohoo.wav"])
        lab.config(text="stop", fg="black", bg="orange", font=("Impact", 18))
    elif (ltime > 0):
        lab.config(text=timer, font=("Impact", 30))
        TIME = ltime - 1
        CLOCKING = fen.after(1000, start, TIME)

lab = Label(fen, text="", fg="black", bg="orange", font=("Impact", 18))
lab.grid(row=1, column=0)


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
    TIME = 10
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


# def start(t = 5):
#     mins, secs = divmod(t, 60)
#     t = '{:02d}:{:02d}'.format(mins,secs)
#     if (i == 1):
#         lab.config(text=str(t), font=("Impact", 30))
#         if (i > 0):
#             fen.after(1000, mins, secs)

# def start(t=15):
    # while t:
    #     mins, secs = divmod(t, 60)
    #     timer ='{:02d}:{:02d}'.format(mins, secs)
    #     lab.config(text=str(t))
    #     time.sleep(1)
    #     lab.config(text=str(t))
    #     t -= 1
    # lab.config(text=str(t))
    # print("Time is out!")


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
