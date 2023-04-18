import tkinter as tk
from tkinter import ttk

class Cardreader(ttk.Frame):
    def __init__(self, master, callback, cards=None):
        ttk.Frame.__init__(self, master)

        self.callback = callback

        self.cardreader = tk.Label(self, text="Зчитувач карток")
        self.cardreader.grid(column=0,row=1)

        self.dropdownvar = tk.StringVar()

        style = ttk.Style()
        style.configure('TCombobox', padding=(5, 5, 5, 5), font=('Helvetica', 8))

        self.dropdown = ttk.Combobox(self, width=30, height=1, textvariable=self.dropdownvar)
        self.dropdown['values'] = cards
        self.dropdown.grid(column=0, row=2)

        self.dropdown.bind("<<ComboboxSelected>>", self.on_menu_select)

    def on_menu_select(self, event):
        selected_value = self.dropdownvar.get()
        print("Selected value:", selected_value)
        self.callback(selected_value)
        self.cardreader.configure(state="disabled")
        self.dropdown.configure(state="disabled")

