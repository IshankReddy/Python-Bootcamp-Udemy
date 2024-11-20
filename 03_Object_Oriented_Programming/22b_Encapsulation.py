class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance  # Getter method

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

account = BankAccount(1000)
print(account.get_balance())  # Access balance via getter
account.deposit(500)          # Modify balance via setter
print(account.get_balance())