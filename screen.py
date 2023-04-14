import tkinter as tk

class Screen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.button1 = tk.Button(self, text="Button 1")
        self.button2 = tk.Button(self, text="Button 2")
        self.label = tk.Label(self, text="Label")
        self.entry = tk.Entry(self)
        
        # розмітка для елементів
        self.button1.grid(row=0, column=0, padx=10, pady=10)
        self.button2.grid(row=1, column=0, padx=10, pady=10)
        self.label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        self.entry.grid(row=1, column=1, padx=10, pady=10)
        
