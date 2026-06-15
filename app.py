from tkinter import *
from time import strftime
from datetime import datetime

# Main Window
root = Tk()
root.title("Smart Digital Clock")
root.geometry("900x500")
root.configure(bg="#0f172a") 
root.resizable(False, False)

# Greeting Function
def get_greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning !"
    elif hour < 18:
        return "Good Afternoon !"
    else:
        return "Good Evening !"

# Update Clock
def update_time():
    current_time = strftime("%I:%M:%S %p")
    current_date = strftime("%d %B %Y")
    current_day = strftime("%A")

    time_label.config(text=current_time)
    date_label.config(text=current_date)
    day_label.config(text=current_day)
    greeting_label.config(text=get_greeting())

    root.after(1000, update_time)

# Title
title = Label(
    root,
    text="SMART DIGITAL CLOCK",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title.pack(pady=20)

# Greeting
greeting_label = Label(
    root,
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="#facc15"
)
greeting_label.pack(pady=5)

# Clock Frame
clock_frame = Frame(
    root,
    bg="#1e293b",
    bd=4,
    relief=RIDGE
)
clock_frame.pack(pady=30, padx=30)

# Time
time_label = Label(
    clock_frame,
    font=("Consolas", 55, "bold"),
    bg="#1e293b",
    fg="#22c55e",
    padx=40,
    pady=20
)
time_label.pack()

# Date
date_label = Label(
    root,
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="#e2e8f0"
)
date_label.pack(pady=10)

# Day
day_label = Label(
    root,
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="#f4effa"
)
day_label.pack()

# Footer
footer = Label(
    root,
    text="Created by SOWMIYAA BGM - Smart Digital Clock App",
    font=("Arial", 12),
    bg="#0f172a",
    fg="#64748b"
)
footer.pack(side=BOTTOM, pady=15)

# Start Clock
update_time()

root.mainloop()