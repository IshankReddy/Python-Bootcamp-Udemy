# main.py
from savings_account import SavingsAccount
from current_account import CurrentAccount
from account import Account

def display_account_details(account):
    print(account.check_balance())

def main():
    # Creating objects for different accounts
    savings_acc = SavingsAccount("Alice", 1000)
    current_acc = CurrentAccount("Bob", 500)

    # Accessing public static variable (bank_name)
    print(f"\n--- Bank: {Account.bank_name} ---\n")

    # Performing operations on SavingsAccount
    print("\n--- Savings Account ---")
    savings_acc.deposit(500)
    savings_acc.add_interest()
    savings_acc.withdraw(300)
    print(savings_acc._get_owner())  
    display_account_details(savings_acc)

    # Performing operations on CurrentAccount
    print("\n--- Current Account ---")
    current_acc.deposit(200)
    current_acc.withdraw(1000)  
    print(current_acc.get_overdraft_limit())
    display_account_details(current_acc)

    # Using the static method to convert currency
    print("\n--- Static Method: Currency Conversion ---")
    amount_in_usd = 100
    conversion_rate = 0.85  
    amount_in_eur = Account.convert_currency(amount_in_usd, conversion_rate)
    print(f"{amount_in_usd} USD is {amount_in_eur} EUR at conversion rate {conversion_rate}.")

if __name__ == "__main__":
    main()
