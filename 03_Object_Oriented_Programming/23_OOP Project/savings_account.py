# savings_account.py
from account import Account  # Importing from the same package

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.__interest_rate = interest_rate  # Private variable

    def add_interest(self):
        interest = self._balance * self.__interest_rate  # Accessing protected variable
        self.deposit(interest)  # Using public method from the base class
        print(f"Interest of {interest} added. Current balance: {self._balance}.")

    def _get_owner(self):
        return f"Savings Account holder: {super()._get_owner()}"
