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
            self.screen.TE2B("Видача готівки\nВведіть суму кратну 100:")
            self.state = self.cash_1
        # баланс
        elif callback == "R1":
            amount = self.db.check_balance(self.current_card, self.PIN)
            self.screen.back("Поточний баланс:\n"+amount)
            self.state = self.back_to_menu
        # поповнення
        elif callback == "R2":
        # вихід
        elif callback == "R3":
    def cash_1(self, callback):
        if callback == "L3":
            self.screen.menu()
            self.screen.clear_entry()
            self.state = self.menu_state
        elif callback == "R3" and self.screen.entry.get().isdigit():
            self.dispense_amount = int(self.screen.entry.get())
            if self.dispense_amount % 100 == 0:
                self.screen.clear_entry()
                self.screen.T2B("Видача готівки\nСума: "+str(self.dispense_amount)+"\nПідтвердити?")
                self.state = self.cash_2
            else:
                self.screen.back("Помилка!\nНеправильна сума\nСума має бути кратна 100")
                self.screen.clear_entry()
                self.state = self.back_to_menu
                del self.dispense_amount

    def cash_2(self, callback):
        if callback == "L3":
            self.menu_state("R0")
            self.screen.clear_entry()
        elif callback == "R3":
            if self.db.reduce_balance(self.current_card, self.PIN, self.dispense_amount):
                self.screen.back("Готівку видано\nСума: "+str(self.dispense_amount))
                self.menu.cash_dispenser.configure(text=util.count_banknotes(self.dispense_amount))
                self.dispense = True
            else:
                self.screen.back("Помилка!\nНедостатньо коштів")
            self.screen.clear_entry()
            self.state = self.back_to_menu
        del self.dispense_amount
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