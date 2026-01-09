"""4. Menu-Driven Bank Account System
Create a base class Account.
Derived classes: SavingsAccount, CurrentAccount.
Use super() for initialization.
Menu options:
1. Deposit
2. Withdraw
3. Check balance
4. Exit
"""


class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount."

    def get_balance(self):
        return f"Account Holder: {self.account_holder}\nBalance: ${self.balance}"


# Derived Classes using super()
class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0):
        # Using super() to call the parent __init__
        super().__init__(account_holder, balance)
        self.interest_rate = 0.02  # 2% Interest


class CurrentAccount(Account):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = 500

    # Overriding withdraw to allow for overdraft
    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            return f"Withdrew ${amount} (Overdraft used). New balance: ${self.balance}"
        return "Transaction declined. Overdraft limit exceeded."


def bank_menu():
    print("Welcome to the Bank Management System")
    name = input("Enter Account Holder Name: ")
    print("Choose Account Type: 1. Savings | 2. Current")
    acc_type = input("Choice: ")

    if acc_type == "1":
        user_account = SavingsAccount(name)
    else:
        user_account = CurrentAccount(name)

    while True:
        print(f"\n--- {type(user_account).__name__} Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            print(user_account.deposit(amt))
        elif choice == "2":
            amt = float(input("Enter withdrawal amount: "))
            print(user_account.withdraw(amt))
        elif choice == "3":
            print(user_account.get_balance())
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    bank_menu()
