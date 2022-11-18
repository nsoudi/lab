import pytest
from account import *

class Test:

    def setup_method(self):
        self.ac1 = Account("01")
        self.ac2 = Account("02")

    def teardown_method(self):
        del self.ac1
        del self.ac2

    def test_init(self):
        assert self.ac1.getname() == "01"
        self.ac1.deposit(5)
        assert self.ac1.getbalance() == 5
        assert self.ac2.getname() == "02"
        self.ac2.deposit(2)
        assert self.ac2.getbalance() == 2

    def test_deposit(self):
        self.ac1.deposit(5)
        assert self.ac1.getbalance() == 5
        self.ac1.deposit(2)
        assert self.ac1.getbalance() == 7
        self.ac1.deposit(0)
        assert self.ac1.getbalance() == 7
        self.ac1.deposit(-100)
        assert self.ac1.getbalance() == 7

        self.ac1.deposit(-5)
        assert self.ac1.getbalance() != 2


        self.ac1.deposit(2.5)
        assert self.ac1.getbalance() == 9.5
        self.ac1.deposit(-2.5)
        assert self.ac1.getbalance() == 9.5
        self.ac1.deposit(0.0)
        assert self.ac1.getbalance() == 9.5

        self.ac1.deposit(-5.0)
        assert self.ac1.getbalance() != 4.5

    def test_withdraw(self):
        self.ac1.deposit(15)

        self.ac1.withdraw(2)
        assert self.ac1.getbalance() == 13
        self.ac1.withdraw(-2)
        assert self.ac1.getbalance() == 13
        self.ac1.withdraw(0)
        assert self.ac1.getbalance() == 13

        self.ac1.withdraw(-5)
        assert self.ac1.getbalance() != 8.0

        self.ac1.withdraw(2.0)
        assert self.ac1.getbalance() == 11.0
        self.ac1.withdraw(-500)
        assert self.ac1.getbalance() == 11.0
        self.ac1.withdraw(0)
        assert self.ac1.getbalance() == 11.0

        self.ac1.withdraw(-5.0)
        assert self.ac1.getbalance() != 6.0




