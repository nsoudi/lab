class Account:

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount <= 0:
            self.__account_balance = amount
            return False
        elif amount > 0:
            self.__account_balance += amount
            return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__account_balance:
            self.__account_balance = amount
            return False

        elif amount > 0:
            self.__account_balance -= amount
            return True

    def getbalance(self):
        return self.__account_balance

    def getname(self):
        return self.__account_name
