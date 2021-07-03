import os
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from emanager.UI.menubar import MenuBar
from emanager.UI.frames import DashBoard
from emanager.utils.directories import UI_ICONS_DIR


def set_title(master, title="eManager"):
    if os.name == "nt":
        master.iconbitmap(f"{UI_ICONS_DIR}/icon.ico")
    master.title(title)


class App(tk.Tk):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        # theme = ttk.Style()
        # themes ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        # theme.theme_use("clam")
        self.geometry("600x250+300+250")
        self.minsize(550, 200)
        set_title(self)
        self.focus_force()

        self.menu = MenuBar(self)
        self.welc_window = DashBoard(
            self, relief=tk.RIDGE, bd=2, highlightcolor="blue"
        )
        self.welc_window.pack(fill=tk.BOTH, expand=True, ipadx=5, ipady=5)


class LoginWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # TODO add forgot username or password option
        self.geometry("350x100+500+200")
        self.resizable(False, False)
        set_title(self)
        frm_input = tk.Frame(self)
        lbl_username = tk.Label(frm_input, text="Username:", pady=5)
        lbl_pass = tk.Label(frm_input, text="Password:", pady=5)
        self.username = tk.Entry(frm_input, width=30)
        self.password = tk.Entry(frm_input, width=30, show="*")

        lbl_username.grid(row=0, column=0)
        self.username.grid(row=0, column=1)
        lbl_pass.grid(row=1, column=0)
        self.password.grid(row=1, column=1)

        self.btn_login = tk.Button(self, text="Login", command=self._login)
        self.bind("<Return>", self._login)
        self.btn_clear = tk.Button(self, text="Clear", command=self._clear)

        frm_input.pack()
        self.btn_login.pack(side="right", padx=10, pady=10)
        self.btn_clear.pack(side="right", padx=10, pady=10)
        self.username.focus_set()

    def _login(self, *args):
        # TODO  store and load password
        USERNAME, PASS = "", ""
        if (self.password.get() == USERNAME) & (self.username.get() == PASS):
            self.destroy()
            app = App()
            app.mainloop()
        else:
            messagebox.showwarning(
                "LoginError", "Invalid Username or Password"
            )

    def _clear(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.username.focus_set()
