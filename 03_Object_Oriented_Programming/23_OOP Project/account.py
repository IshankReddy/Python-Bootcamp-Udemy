# account.py

class Account:
    # Static public variable: available to the class and all instances
    bank_name = "Global Bank"  # Public static variable

    def __init__(self, owner, balance=0):
        self.__owner = owner         # Private variable (name mangling)
        self._balance = balance      # Protected variable (accessible in derived classes)
        self.__account_number = self.__generate_account_number()  # Private method to generate account number
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. Remaining balance is {self._balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    # Public method to check balance (uses a private method internally)
    def check_balance(self):
        return self.__display_balance()   # Calling private method from public method

    # Private method: Accessible only within the class
    def __display_balance(self):
        return f"{self.__owner}'s account balance is {self._balance}. Account Number: {self.__account_number}"

    # Protected method: Can be used by derived classes
    def _get_owner(self):
        return self.__owner

    # Static method: Utility to convert currency, does not depend on instance data
    @staticmethod
    def convert_currency(amount, rate):
        return amount * rate

    # Private static method: Used internally for generating account numbers
    @staticmethod
    def __generate_account_number():
        from random import randint
        return randint(100000, 999999)