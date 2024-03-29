import csv

def pin_required(func):
        def wrapper(self, *args, **kwargs):
            if self.check_card(*args[:2], **kwargs):
                return func(self, *args, **kwargs)
            else:
                return -1
        return wrapper

class BankDatabase:
    def __init__(self):
        self.parse_db()

    def parse_db(self):
        self.db = {}
        with open('db.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                card = row['Card']
                self.db[card] = row

    def check_card(self, card, pin):
        if self.db[card] and self.db[card]["PIN"]==pin:
            return True
        else:
            return False

    @pin_required
    def check_balance(self, card, pin):
        return self.db[card]["Balance"]

    @pin_required
    def reduce_balance(self, card, pin, amount):
        balance = int(self.db[card]["Balance"])
        if balance - amount >= 0:
            self.db[card]["Balance"] = str(balance-amount)
            return True
        else:
            return False
