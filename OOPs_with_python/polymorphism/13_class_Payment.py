"""Create a base class Payment with pay(). Derive UPI, Card, and Wallet. Process payments polymorphically."""

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement pay()")

class UPI(Payment):
    def pay(self, amount):
        print("Paying", amount, "via UPI")

class Card(Payment):
    def pay(self, amount):
        print("Paying", amount, "via Card")

class Wallet(Payment):
    def pay(self, amount):
        print("Paying", amount, "via Wallet")

def process_payment(payment_method: Payment, amount):
    payment_method.pay(amount)

methods = [UPI(), Card(), Wallet()]

for m in methods:
    process_payment(m, 1000)



    