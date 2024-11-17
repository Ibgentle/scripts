#!/usr/bin/python3

__author__ = "Ibor Offor"
__designation__ = "Technical Manager"
__email__ = "iboroffor@gmail.com"

from GetVoiceRecordings import recordings
from tkinter import * 
from tkinter.ttk import *


"""
    A GUI program to get Voice Recordings from the Server.
    I know that asterisk imports are a terrible idea,
    but it's done above so that native (old) tkinter
    widgets can be replaced automatically by their
    modern and more beatuitful (themed) alternatives
    in the ttk module.
"""

window = Tk()
window.title("Get Voice Recordings")
window.resizable(False, False)

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

def get_records():
    phone_num = entry_phone.get()
    date_input = entry_date.get()
    recordings(phone_num, date_input)
    label_records = Label(master=frame, text="Done! Go to 'C:/Users/Public/Downloads' to see the files.", foreground="red")
    return label_records.pack()

frame = Frame(relief=RAISED, height=100, width=100, borderwidth=5, pad=50)
btn = Button(master=frame, text="Get Recordings", pad=5, command=get_records)

entry_phone = Entry(master=frame)
label_phone = Label(master=frame, text="Enter phone number without leading zero (0): ", foreground="#167a78", pad=5)

entry_date = Entry(master=frame)
label_date = Label(master=frame, text="Enter date in the format YYYY/MM/DD: ", foreground="#167a78", pad=5)

frame.pack()

label_phone.pack()
entry_phone.pack()
label_date.pack()
entry_date.pack()
btn.pack(pady=5)


window.mainloop()

