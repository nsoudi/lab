#collaboraters on this assignment are Noe Soudi and Tiffany Domingo
class Account:
    """
    A class representing a banking account for an account object


    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create the initial state of a class object
        :param name: Name of the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit and increment an account's balance
        :param amount: Amount being deposited into an accounts balance
        :return: True or False boolean depending on whether the deposit was successful or not
        """
        if amount <= 0:
            amount = self.__account_balance
            return False
        elif amount > 0:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw and decrement an account's balance
        :param amount: Amount being withdrawn from an accounts balance
        :return: True or False boolean depending on whether the withdrawl was successful or not
        """
        if amount <= 0 or amount > self.__account_balance:
            amount = self.__account_balance
            return False

        elif amount > 0:
            self.__account_balance -= amount
            return True

    def getbalance(self) -> float:
        """
        Method to access an account's current balance
        :return: Account's current balance
        """
        return self.__account_balance

    def getname(self) -> str:
        """
        Method to access the name of an account
        :return: Account's current balance
        """
        return self.__account_name
