from tkinter import Tk
from tkinter import Label
import time
import sys


master = Tk()
master.title("Digital Clock")


def get_time():
    timeVar = time.strftime("%A:%I:%M:%S: %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)


clock = Label(master, font=("Calibri", 70), bg="black", width=19, fg="white")
clock.pack()

get_time()


master.mainloop()
