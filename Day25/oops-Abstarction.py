#abstraction
from abc import ABC,abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")
    def viewhistory(self):
        print("You can  your transactions")
    def userinfo(self):
        print("You can see your details")
    def transactions(self):
        print("You can transfer money through netbanking")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    
class CurrentAccount(BankAccount):
    def deposit(self):
        print("You can deposit - CA")
    def withdraw(self):
        print("You can withdraw - CA")

class SavingAccount(BankAccount):
    def deposit(self):
        print("You can deposit - SA")
    def withdraw(self):
        print("You can withdraw - SA")
class FixedDeposit(BankAccount):
    def fixeddeposit(self):
        print("You can deposit - FD")
    def withdraw(self):
        print("You can withdraw - FD")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("You can deposit - SAA")
    def withdraw(self):
        print("You can withdraw - SAA")
class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("You can deposit - ZBA")
    def withdraw(self):
        print("You can withdraw - ZBA")
hemanth=ZeroBalanceAccount()
hemanth.deposit()
hemanth.withdraw()
hemanth.checkbalance()
hemanth.viewhistory()
hemanth.userinfo()
hemanth.transactions()

sekhar=SalaryAccount()
sekhar.deposit()
sekhar.withdraw()
sekhar.checkbalance()
sekhar.viewhistory()
sekhar.userinfo()
sekhar.transactions()
