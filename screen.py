import tkinter as tk

class Screen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.button1 = tk.Button(self, text="Button 1", state="disabled")
        self.button2 = tk.Button(self, text="Button 2", state="disabled")
        self.button3 = tk.Button(self, text="Button 3", state="disabled")
        self.button4 = tk.Button(self, text="Button 4", state="disabled")
        self.button5 = tk.Button(self, text="Button 5", state="disabled")
        self.button6 = tk.Button(self, text="Button 6", state="disabled")
        self.label = tk.Label(self, text="Label")
        self.entry = tk.Entry(self, state="disabled")
        
        # розмітка для елементів
        self.button1.grid(row=0, column=0, padx=10, pady=10)
        self.button2.grid(row=1, column=0, padx=10, pady=10)
        self.label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        self.entry.grid(row=1, column=1, padx=10, pady=10)
        self.button5.grid(row=2, column = 0, padx=10, pady=10)
        self.button6.grid(row=2, column = 1, padx=10, pady=10)
        
        # початковий стан
        self.set_state("4B")

    def set_entry_text(self, text, mode):
        self.entry.configure(state="normal")
        if (mode == "d"):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, text)
        elif (mode == "a"):
            self.entry.insert(0, text)
        self.entry.configure(state="disabled")

    def set_state(self, state):
        # прибрати усі елементи
        self.button1.grid_remove()
        self.button2.grid_remove()
        self.button3.grid_remove()
        self.button4.grid_remove()
        self.button5.grid_remove()
        self.button6.grid_remove()
        self.label.grid_remove()
        self.entry.grid_remove()
        
        if state == "4B":
            self.button1.grid()
            self.button2.grid()
            self.button3.grid()
            self.button4.grid()
        elif state == "T":
            self.label.config(text="Text")
            self.label.grid()
        elif state == "TE":
            self.label.config(text="Text")
            self.label.grid()
            self.entry.grid()
        elif state == "T2B":
            self.label.config(text="Text")
            self.label.grid()
            self.button1.grid()
            self.button2.grid()
        elif state == "TE2B":
            self.label.config(text="Text")
            self.label.grid()
            self.entry.grid()
            self.button1.grid()
            self.button2.grid()

