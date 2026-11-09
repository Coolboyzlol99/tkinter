from tkinter import *

root = Tk()
root.title("Event Handler")
root.geometry("100x100")

def handle_keypress(event):
    """Print the character associated with the key pressed."""
    print(event.char)

root.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked")

bt1 = Button(root, text="Click Me")
bt1.pack()
bt1.bind("<Button-1>", handle_click)

root.mainloop()
