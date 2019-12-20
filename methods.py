import datetime
import pytz

class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        print("Account created for "+ self._name)
        self._transaction_list.append((Account._current_time(), self.__balance)) 
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        self.show_balance()
        self._transaction_list.append((Account._current_time(), amount)) # In place of Account._current_time() self._current_time() can also be used but it increased the time complexity

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than 0 and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1

            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    kush = Account("Kush", 0)
    kush.show_balance()

    kush.deposit(1000)
    kush.show_balance()
    kush.withdraw(500)
    kush.show_balance()
    kush.withdraw(555555)
    kush.show_transactions()

    rimmi = Account("Rimmi", 800)
    rimmi.deposit(100)
    rimmi.__balance = 20000000
    rimmi.withdraw(200)
    rimmi.show_transactions()
    print(rimmi.__dict__)
    rimmi._Account__balance = 3333
    rimmi.show_balance()