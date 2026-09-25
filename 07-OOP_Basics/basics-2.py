from abc import ABC, abstractmethod


class BankAccount(ABC):

    bank_name = "SimBank"

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.01


account1 = SavingsAccount("SB101", "Sim", 10000)

account1.deposit(2000)
account1.withdraw(3000)

print("Balance:", account1.balance)
print("Interest:", account1.calculate_interest())