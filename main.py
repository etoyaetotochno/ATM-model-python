import tkinter as tk
from menu import Menu
class ATMApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.title("ATM App")
        self.menu = Menu(self.root, callback=self.menu_callback)
    def menu_callback(self, callback):
        self.update_screen(callback)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    atm_app = ATMApp()
    atm_app.run()