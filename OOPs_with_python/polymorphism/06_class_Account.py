"""
Create a base class Account with interest(). Derive SavingsAccount and CurrentAccount. 
Call interest() using a base class reference.
"""
class Account:
    def interest(self):
        raise NotImplementedError("Subclass must implement interest()")

class SavingsAccount(Account):
    def interest(self):
        return 4.0  # percent

class CurrentAccount(Account):
    def interest(self):
        return 0.5  # percent

def show_interest(acc: Account):
    print(type(acc).__name__, "interest rate:", acc.interest(), "%")

a: Account

a = SavingsAccount()
show_interest(a)

a = CurrentAccount()
show_interest(a)
