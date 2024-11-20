# current_account.py
from account import Account  # Importing from the same package

class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit  # Protected variable

    def withdraw(self, amount):
        if 0 < amount <= (self._balance + self._overdraft_limit):
            self._balance -= amount
            print(f"Withdrew {amount}. Remaining balance is {self._balance}.")
        else:
            print("Overdraft limit exceeded.")

    def get_overdraft_limit(self):
        return f"Overdraft limit is {self._overdraft_limit}"
