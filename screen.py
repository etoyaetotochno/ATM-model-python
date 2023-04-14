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
        
        # початковий стан
        self.set_state("buttons")
        
    def set_state(self, state):
        # прибрати усі елементи
        self.button1.grid_remove()
        self.button2.grid_remove()
        self.label.grid_remove()
        self.entry.grid_remove()
        
        if state == "buttons":
            self.button1.grid()
            self.button2.grid()
        elif state == "text":
            self.label.config(text="Text")
            self.label.grid()
        elif state == "text_and_input":
            self.label.config(text="Text")
            self.label.grid()
            self.entry.grid()
        elif state == "text_and_2_buttons":
            self.label.config(text="Text")
            self.label.grid()
            self.button1.grid()
            self.button2.grid()
        elif state == "text_and_entry_and_2_buttons":
            self.label.config(text="Text")
            self.label.grid()
            self.entry.grid()
            self.button1.grid()
            self.button2.grid()

