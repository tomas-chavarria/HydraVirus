from tkinter import *
from tkinter import ttk

def on_closing(r):
    r.destroy()

    for i in range(3):
        create_window()

def create_window():
    # Initializes the executable window
    root = Tk()
    root.title("Hydra.exe")

    # Generates the label and quit button for the program
    ttk.Label(root, text="Cut off one head, three more grow back").pack()
    ttk.Button(root, text="QUIT", command=lambda arg=root: on_closing(arg)).pack()

    root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))



#Initializes the executable window
root = Tk()
root.title("Hydra.exe")

#Generates the label and quit button for the program
ttk.Label(root, text="Cut off one head, three more grow back").pack()
ttk.Button(root, text="QUIT", command=lambda arg=root: on_closing(arg)).pack()

root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))
mainloop()