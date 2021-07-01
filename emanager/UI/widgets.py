import tkinter as tk


class ImgButton(tk.Button):
    # PROBLEM images are not shown in the buttons
    def __init__(self, master, icon_path="", **kw):
        super().__init__(master, relief=tk.RAISED, compound="top", **kw)
        self.icon = tk.PhotoImage(icon_path).subsample(4, 4)
        self.image = self.icon
        # borderwidth=0,


class LinkButton(tk.Button):
    def __init__(self, *args, **kw):
        super().__init__(
            *args,
            fg="blue",
            cursor="hand2",
            justify="left",
            font=("Calibri", 10, tk.UNDERLINE),
            activebackground="violet",
            relief=tk.FLAT,
            **kw,
        )
        self.bind("<Enter>", lambda event: self.config(fg="green"))
        self.bind("<Leave>", lambda event: self.config(fg="blue"))
