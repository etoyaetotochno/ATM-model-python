import tkinter as tk
from tkinter import ttk
from ScreenDecorators import clear, entry

class Screen(ttk.Frame):
    def __init__(self, master):
        
        ttk.Frame.__init__(self, master)

        self.button1 = tk.Button(self, text="Button 1", state="disabled", disabledforeground="black", relief=tk.SOLID, width=8, height=1)
        self.button2 = tk.Button(self, text="Button 2", state="disabled", disabledforeground="black", relief=tk.SOLID, width=8, height=1)
        self.button3 = tk.Button(self, text="Button 3", state="disabled", disabledforeground="black" ,relief=tk.SOLID, width=8, height=1)
        self.button4 = tk.Button(self, text="Button 4", state="disabled", disabledforeground="black", relief=tk.SOLID, width=8, height=1)
        self.button5 = tk.Button(self, text="Назад", state="disabled", disabledforeground="black", relief=tk.SOLID, width=8, height=1)
        self.button6 = tk.Button(self, text="Далі", state="disabled", disabledforeground="black", relief=tk.SOLID, width=8, height=1)
        self.message = tk.Message(self, justify=tk.CENTER, width=150)
        self.entry = tk.Entry(self, relief=tk.SOLID, state="disabled")

        self.elements = (self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.message, self.entry)

        self.button5.grid(row=3, column = 0, sticky='w', padx=10, pady=12)
        self.button6.grid(row=3, column = 1, sticky='e', padx=10, pady=12)

    def set_entry_text(self, text, mode):
        if self.entry_visible:
            self.entry.configure(state="normal")
            if (mode == "d"):
                self.clear_entry()
                self.entry.insert(0, text)
            elif (mode == "a"):
                self.entry.insert(0, text)
            self.entry.configure(state="disabled")

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    # states
    @clear
    def T(self, text):
        self.message.config(text=text)
        self.message.grid(row=0, column=0, columnspan=2, rowspan=4, padx=10, pady=10)
        self.grid(sticky="ew")

    @clear
    @entry
    def TE(self, text):
        self.message.config(text=text)
        self.message.grid(row=0, column=0, columnspan=2, rowspan=3, padx=10, pady=10)
        self.entry.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    @clear
    def T2B(self, text):
        self.message.config(text=text)
        self.message.grid(row=0, column = 0, columnspan=2, rowspan=3, padx=10, pady=10)
        self.button5.grid()
        self.button6.grid()

    @clear
    @entry
    def TE2B(self, text):
        self.message.config(text=text)
        self.message.grid(row=0, column = 0, columnspan=2, rowspan=2, padx=10, pady=10)
        self.entry.grid(row=2, column = 0, columnspan=2, padx=10, pady=10)
        self.button5.grid()
        self.button6.grid()

    @clear
    def menu(self):
        self.button1.grid(row=0, column=0, sticky="ne", padx=10, pady=12)
        self.button2.grid(row=1, column=0, sticky="ne", padx=10, pady=12)
        self.button3.grid(row=2, column=0, sticky="ne", padx=10, pady=12)
        self.button4.grid(row=3, column=0, sticky="ne", padx=10, pady=12)
        
