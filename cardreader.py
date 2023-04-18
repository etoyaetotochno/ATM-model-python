import tkinter as tk
from tkinter import ttk

class Cardreader(ttk.Frame):
    def __init__(self, master, callback, cards=None):
        ttk.Frame.__init__(self, master)

        self.callback = callback
