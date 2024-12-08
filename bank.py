from abc import ABC

class Account(ABC):
    accounts = []

    def __init__(self, name, accNo, password, type):
        self.name = name
        self.accNum = accNo
        self.password = password
        self.balance = 0
        self.type = type

        Account.accounts.append(self)

    def changeInfo(self, newName):
        self.name = newName
        print(f"Name change to {newName}")

    def changeInfo(self, newName, newPass):
        self.name = newName
        self.password = newPass
        print(f"Name change to {newName} and password  is: {newPass}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"your balance is now {amount}")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"After withdraw your balance is Now {amount}")
   
    @classmethod
    def showInfo(self):
        pass

class SavingsAccount(Account):
    def __init__(self, name, accNo, password, type, irate):
        super().__init__(name, accNo, password, type)
        self.interestRate = irate

myAccount = Account("Habib", 1234, 5678, "Savings")
myAccount.changeInfo("Shaifan", 234)
myAccount.deposit(500)
myAccount.withdraw(100)