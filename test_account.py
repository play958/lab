from pytest import *
from account import *
class Test:
    def setup_method(self):
        self.a1 = Account('Jimbo')

    def teardown_method(self):
        del self.a1


    def test_init(self):
        assert self.a1.get_name() == 'Jimbo'
        assert self.a1.get_balance() == 0


    def test_deposit(self):
        assert self.a1.deposit(-100) == False
        assert self.a1.deposit(0) == False
        assert self.a1.deposit(100) == True
        assert self.a1.deposit(9.70) == True


    def test_withdraw(self):
        self.a1.deposit(100)
        assert self.a1.withdraw(-100) == False
        assert self.a1.withdraw(0) == False
        assert self.a1.withdraw(110) == False
        assert self.a1.withdraw(99) == True


