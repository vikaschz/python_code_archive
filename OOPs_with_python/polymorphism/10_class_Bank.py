"""Create a base class Bank with rate_of_interest(). Derive SBI, HDFC, and ICICI. Display interest rates using polymorphism."""
class Bank:
    def rate_of_interest(self):
        raise NotImplementedError("Subclass must implement rate_of_interest()")

class SBI(Bank):
    def rate_of_interest(self):
        return 6.5

class HDFC(Bank):
    def rate_of_interest(self):
        return 7.0

class ICICI(Bank):
    def rate_of_interest(self):
        return 6.8

banks = [SBI(), HDFC(), ICICI()]

for b in banks:
    print(type(b).__name__, "ROI:", b.rate_of_interest(), "%")
