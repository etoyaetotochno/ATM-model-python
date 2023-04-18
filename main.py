import tkinter as tk
from menu import Menu
from screen import Screen
from cardreader import Cardreader
from bankdatabase import BankDatabase
import util

class ATMApp:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("380x520")
        self.root.title("ATM App")
        self.menu = Menu(self.root, callback=self.menu_callback)

        self.screen = Screen(self.menu.screen_frame)
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_rowconfigure(0, weight=1)

        # початковий стан
        self.screen.T("Вставте картку")
        self.state = None

        # завантажити карти
        self.parse_cards()

        # завантажити базу даних
        self.db = BankDatabase()

        # зчитувач карток
        self.cardreader = Cardreader(self.menu.mainframe, cards=self.credit_cards, callback=self.cardreader_callback)
        self.cardreader.grid(column=0, row=2, padx=10, pady=10)

    def menu_callback(self, callback):
        if self.screen.entry_visible:
            try:
                if int(callback) in range(0,10):
                    self.screen.set_entry_text(callback)
            except:
                # очищення тексту
                if self.screen.entry_visible and callback == "КОРР":
                    self.screen.clear_entry()
        if self.state:
            self.state(callback)

    def cardreader_callback(self, callback):
        self.current_card = callback
        self.screen.TE(text="Введіть пін-код")
        self.state = self.pin

    def pin(self, callback):
        if callback == "ОК":
            self.PIN = self.screen.entry.get()
            if self.db.check_card(self.current_card, self.PIN):
                self.screen.clear_entry()
                self.screen.menu()
                self.state = self.menu_state
            else:
                self.screen.TE("Неправильний пін-код\nСпробуйте ще раз")
                self.screen.clear_entry()

    def menu_state(self, callback):
        # видача готівки
        if callback == "R0":
        # баланс
        elif callback == "R1":
        # поповнення
        elif callback == "R2":
        # вихід
        elif callback == "R3":
            self.screen.menu()

    def parse_cards(self):
        self.credit_cards = []
        with open('cards.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                card_number = line.strip()
                if util.luhn(card_number):
                    self.credit_cards.append(card_number)

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    atm_app = ATMApp()
    atm_app.run()