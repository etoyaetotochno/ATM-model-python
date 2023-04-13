import tkinter as tk
from tkinter import ttk
class Menu:
    def __init__(self, root):
        self.root = root

        # головний фрейм
        self.mainframe = ttk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.mainframe.grid(column=0, row=0)

        # фрейм для екрану
        self.screen_place = ttk.Frame(self.mainframe, padding="5 5 5 5", relief=tk.RAISED, borderwidth=1)
        self.screen_place.grid(column=0, row=0)

        #фрейм для вмісту екрану
        self.screen_frame = ttk.Frame(self.screen_place, width=200, height=200, relief=tk.RAISED, borderwidth=1)
        self.screen_frame.grid(column=1, row=0, rowspan=4, sticky="nsew")
