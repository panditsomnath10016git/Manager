import tkinter as tk
from emanager.UI.widgets import LinkButton, ImgButton
from emanager.utils.directories import UI_ICONS_DIR


class QuickLinks(tk.LabelFrame):
    def __init__(self, *args, **kw):
        super().__init__(
            *args,
            text="Quick Links",
            font=("Times New Roman", 12),
            relief=tk.GROOVE,
            **kw,
        )
        self.add_cstmr = LinkButton(self, text="Add Customer")
        self.wrkr_atndnc = LinkButton(self, text="Worker Attendance")
        self.finance_stat = LinkButton(self, text="Finance Status")

        self.add_cstmr.pack(anchor="w")
        self.wrkr_atndnc.pack(anchor="w")
        self.finance_stat.pack(anchor="w")


class ModuleLinks(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_rowconfigure([0, 1], weight=1)
        self.grid_columnconfigure([0, 1, 2, 3], weight=1)
        self.modules = [
            "sell",
            "buy",
            "HR",
            "accounting",
            "CRM",
            "production",
            "tools",
        ]
        colors = [
            "SpringGreen",
            "plum1",
            "Gold",
            "cyan",
            "RoyalBlue1",
            "salmon1",
            "magenta2",
        ]
        self.buttons = []
        self.icons = []
        row, col = 0, 0
        n_columns = 4  # number of columns
        for module, color in zip(self.modules, colors):
            if col > n_columns - 1:
                col = 0
                row += 1
            icon = tk.PhotoImage(
                f"{UI_ICONS_DIR}/{module}/icon.png"
            ).subsample(4, 4)
            button = tk.Button(
                self,
                text=module,
                image=icon,
                bg=color,
                # relief=tk.RAISED,
                compound="top",
                width=80,
            )
            button.grid(
                column=col,
                row=row,
                sticky="nsew",
                padx=5,
                pady=5,
            )
            col += 1
            self.icons += [icon]
            self.buttons += [button]


class DashBoard(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1)

        self.qik_lnks = QuickLinks(self)
        self.module_frame = ModuleLinks(
            self, bg="lavender", relief=tk.GROOVE, borderwidth=4
        )

        self.qik_lnks.grid(
            row=0, column=0, padx=10, pady=5, ipady=10, sticky="nsew"
        )  # padx=10, pady=10,
        self.module_frame.grid(
            row=0, column=1, ipadx=5, ipady=5, sticky="nsew"
        )
