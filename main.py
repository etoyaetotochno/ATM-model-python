import tkinter as tk
from menu import Menu
from screen import Screen

class ATMApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.title("ATM App")
        self.menu = Menu(self.root, callback=self.menu_callback)

        self.screen = Screen(self.menu.screen_frame)
        self.screen.grid(sticky="sew")
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_rowconfigure(0, weight=1)

        # початковий стан
        self.screen.menu()

    def menu_callback(self, callback):
        self.update_screen(callback)

    # передача на екран
    def update_screen(self, value):
        if (value=="1"):
            self.screen.menu()
        elif (value=="2"):
            self.screen.TE(text="text")
        elif (value=="3"):
            self.screen.T2B(text="text")
        elif (value=="4"):
            self.screen.TE2B(text="text")
        elif (value=="5"):
            self.screen.set_entry_text("A","a")
        elif (value=="6"):
            self.screen.set_entry_text("A","d")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    atm_app = ATMApp()
    atm_app.run()