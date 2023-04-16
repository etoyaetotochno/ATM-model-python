import tkinter as tk

class Screen(tk.ttk.Frame):
    def __init__(self, master):
        tk.ttk.Frame.__init__(self, master)

        self.button1 = tk.Button(self, text="Button 1", state="disabled", width=8, height=1)
        self.button2 = tk.Button(self, text="Button 2", state="disabled", width=8, height=1)
        self.button3 = tk.Button(self, text="Button 3", state="disabled", width=8, height=1)
        self.button4 = tk.Button(self, text="Button 4", state="disabled", width=8, height=1)
        self.button5 = tk.Button(self, text="Button 5", state="disabled", width=8, height=1)
        self.button6 = tk.Button(self, text="Button 6", state="disabled", width=8, height=1)
        self.message = tk.Message(self, justify=tk.CENTER, width=150)
        self.entry = tk.Entry(self, state="disabled")

        self.elements = (self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.message, self.entry)

        self.button5.grid(row=3, column = 0, sticky='w', padx=10, pady=10)
        self.button6.grid(row=3, column = 1, sticky='e', padx=10, pady=10)

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
    def T(self, text):
        self.clear_elements()
        self.message.config(text=text)
        self.message.grid()

    def TE(self, text):
        self.clear_elements()
        self.entry_visible = True
        self.message.config(text=text)
        self.message.grid(row=0, column=0, columnspan=2, rowspan=3, padx=10, pady=10)
        self.entry.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def T2B(self, text):
        self.clear_elements()
        self.message.config(text=text)
        self.message.grid(row=0, column = 0, columnspan=2, rowspan=3, padx=10, pady=10)
        self.button5.grid()
        self.button6.grid()

    def TE2B(self, text):
        self.clear_elements()
        self.entry_visible = True
        self.message.config(text=text)
        self.message.grid(row=0, column = 0, columnspan=2, rowspan=2, padx=10, pady=10)
        self.entry.grid(row=2, column = 0, columnspan=2, padx=10, pady=10)
        self.button5.grid()
        self.button6.grid()

    def menu(self):
        self.clear_elements()
        self.button1.grid(row=0, column=0, sticky="E", padx=10, pady=10)
        self.button2.grid(row=1, column=0, sticky="E", padx=10, pady=10)
        self.button3.grid(row=2, column=0, sticky="E", padx=10, pady=10)
        self.button4.grid(row=3, column=0, sticky="E", padx=10, pady=10)
        
    def clear_elements(self):
        for element in self.elements:
            element.grid_remove()
        self.entry_visible = False

