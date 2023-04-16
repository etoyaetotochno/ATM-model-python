import tkinter as tk
from tkinter import ttk

class Menu:
    def __init__(self, root, callback):
        
        self.root = root
        self.callback = callback

        # головний фрейм
        self.mainframe = ttk.Frame(self.root, relief=tk.RAISED)
        self.mainframe.grid()

        # фрейм для екрану
        self.screen_place = ttk.Frame(self.mainframe, relief=tk.RAISED, borderwidth=1)
        self.screen_place.grid()

        #фрейм для вмісту екрану
        self.screen_frame = ttk.Frame(self.screen_place, width=200, height=200)
        self.screen_frame.grid(column=1, row=0, columnspan=2, rowspan=4)
        self.screen_frame.grid_columnconfigure(0, weight=1)
        self.screen_frame.grid_rowconfigure(0, weight=1)
        self.screen_frame.grid_propagate(False)

        # кнопки зліва від екрану
        for i in range(4):
            button = tk.Button(self.screen_place, text=">>", width=10, height=2, command=lambda v="L"+str(i): self.button_clicked(v))
            button.grid(row=i, column=0, padx=5)

        # кнопки справа від екрану
        for i in range(4):
            button = tk.Button(self.screen_place, text="<<", width=10, height=2, command=lambda v="R"+str(i): self.button_clicked(v))
            button.grid(row=i, column=3, padx=5)

        # зчитувач карток
        self.cardreader = tk.Label(self.mainframe, text="Зчитувач карток", width=20, height=2, relief=tk.RAISED, borderwidth=1)
        self.cardreader.grid(column=0,row=2)

        # фрейм для кнопок
        self.pinpad = tk.Frame(self.mainframe, width=200, height=200, relief=tk.RAISED, borderwidth=1)
        self.pinpad.grid(column=0,row=3)

        # нумеровані кнопки
        for i in range(3):
            for j in range(3):
                value = i * 3 + j + 1
                button = tk.Button(self.pinpad, text=str(value), width=10, height=2, command=lambda v=str(value): self.button_clicked(v))
                button.grid(row=i, column=j, padx=5, pady=5)

        # бокові кнопки
        side_buttons = ["СКАС", "КОРР", "ВІДМ", "ОК"]
        for i in range(4):
            button = tk.Button(self.pinpad, text=side_buttons[i], width=10, height=2, command=lambda v=side_buttons[i]: self.button_clicked(v))
            button.grid(row=i, column=3, padx=5, pady=5)

        # нижні кнопки 0, 00
        button_text = ["", "0", "00"]
        for i in range(3):
            button = tk.Button(self.pinpad, text=button_text[i], width=10, height=2, command=lambda v=button_text[i]: self.button_clicked(v))
            button.grid(row=3, column=i, padx=5, pady=5)

        # видавач готівки
        self.cash_dispenser = tk.Label(self.mainframe, text="Видавач готівки", width=40, height=2, relief="sunken")
        self.cash_dispenser.grid(column=0,row=4)

    # натиск кнопки
    def button_clicked(self, value):
        print(f"Button {value} clicked")
        self.callback(value)

