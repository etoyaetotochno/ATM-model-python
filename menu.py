import tkinter as tk
from tkinter import ttk
class Menu:
    def __init__(self, root):
        self.root = root

        # головний фрейм
        self.mainframe = ttk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.mainframe.grid(column=0, row=0)
