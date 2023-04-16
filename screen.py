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
        
        # початковий стан
        self.set_state("4B")

    def set_entry_text(self, text, mode):
        if self.state == "TE" or self.state == "TE2B":
            self.entry.configure(state="normal")
            if (mode == "d"):
                self.clear_entry()
                self.entry.insert(0, text)
            elif (mode == "a"):
                self.entry.insert(0, text)
            self.entry.configure(state="disabled")

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def set_state(self, state):
        self.state = state

        self.button5.grid(row=3, column = 0, sticky='w', padx=10, pady=10)
        self.button6.grid(row=3, column = 1, sticky='e', padx=10, pady=10)

        # прибрати усі елементи
        self.button1.grid_remove()
        self.button2.grid_remove()
        self.button3.grid_remove()
        self.button4.grid_remove()
        self.button5.grid_remove()
        self.button6.grid_remove()
        self.message.grid_remove()
        self.entry.grid_remove()
        
        if state == "4B":
            self.button1.grid(row=0, column=0, sticky="E", padx=10, pady=10)
            self.button2.grid(row=1, column=0, sticky="E", padx=10, pady=10)
            self.button3.grid(row=2, column=0, sticky="E", padx=10, pady=10)
            self.button4.grid(row=3, column=0, sticky="E", padx=10, pady=10)
        elif state == "T":
            self.message.config(text="Text")
            self.message.grid()
        elif state == "TE":
            self.message.config(text="ЦЕ ТЕ")
            self.message.grid(row=0, column=0, columnspan=2, rowspan=3, padx=10, pady=10)
            self.entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        elif state == "T2B":
            self.message.config(text="це Т2В")
            self.message.grid(row=0, column = 0, columnspan=2, rowspan=3, padx=10, pady=10)
            self.button5.grid()
            self.button6.grid()
        elif state == "TE2B":
            self.message.config(text="це ТЕ2В, довгий текст")
            self.message.grid(row=0, column = 0, columnspan=2, rowspan=2, padx=10, pady=10)
            self.entry.grid(row=2, column = 0, columnspan=2, padx=10, pady=10)
            self.button5.grid()
            self.button6.grid()
        
