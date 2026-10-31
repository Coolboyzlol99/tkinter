from tkinter import *
from datetime import date

root = Tk()
root.title("Start Widgets")
root.geometry("400x300")

lbl = Label(text = "Hello", fg = "white", bg = "black", height = 1, width = 100)

name_lbl = Label(text = "Full Name", bg = "grey")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application \n Today's date is: "
    greet = "Hello " + name + "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 5)

btn = Button(text = "Submit", command = display, height = 1, bg = "blue", fg = "white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()