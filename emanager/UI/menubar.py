import tkinter as tk
from tkinter import messagebox


class MenuBar:
    def __init__(self, master) -> None:
        menu = tk.Menu(master)
        master.config(menu=menu)
        filemenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)
        for label in ["New", "Open..", "Save", "Save As.."]:
            filemenu.add_command(label=label)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)

        helpmenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=helpmenu)
        for label, command in zip(
            ["Help", "About"], [self.mnu_help, self.mnu_about]
        ):
            helpmenu.add_command(label=label, command=command)

    def mnu_help(self):
        messagebox.showinfo("Help", "There are help options")

    def mnu_about(self):
        messagebox.showinfo("About", "eManager\nVersion 0.0.1")
