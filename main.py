import tkinter as tk
class ATMApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ATM App")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    atm_app = ATMApp()
    atm_app.run()