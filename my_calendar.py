import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

def add_event():
    event_date = cal.selection_get()
    event_description = event_entry.get()
    if event_description:
        event_listbox.insert(tk.END, f"{event_date}: {event_description}")
        event_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("warning", "you need to enter an event description.")

def clear_events():
    event_listbox.delete(0,tk.END)

root = tk.Tk()
root.title("THe Calendar App")

#This will create calendar widget
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)

#This will add events and buttons
event_entry = tk.Entry(root, width=50)
event_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Event", command=add_event)
add_btn.pack(pady=5)

#This willl create listbox
event_listbox = tk.Listbox(root, width=50, height=10)
root.mainloop()
    