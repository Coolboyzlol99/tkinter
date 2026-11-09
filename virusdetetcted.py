from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Detected")
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus found.")

bt1 = Button(root, text="Scan for viruses", command=msg)
bt1.place(x=40, y=80)

root.mainloop()