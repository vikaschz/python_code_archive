"""
Create two base classes OnlinePayment and DeliveryService. Derive Order class using multiple inheritance.
"""


class OnlinePayment:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        self.payment_status = "Pending"

    def process_payment(self, amount):
        print(f"Processing {self.payment_method} payment of ${amount}...")
        self.payment_status = "Completed"
        print("Payment successful!")


class DeliveryService:
    def __init__(self, carrier):
        self.carrier = carrier
        self.shipping_status = "Not Shipped"

    def schedule_delivery(self, address):
        self.shipping_status = "Dispatched"
        print(f"Package handed over to {self.carrier}. Shipping to: {address}")


class Order(OnlinePayment, DeliveryService):
    def __init__(self, order_id, payment_method, carrier):
        OnlinePayment.__init__(self, payment_method)
        DeliveryService.__init__(self, carrier)
        self.order_id = order_id

    def finalize_order(self, amount, address):
        print(f"--- Finalizing Order #{self.order_id} ---")
        self.process_payment(amount)
        self.schedule_delivery(address)
        print("Order status: All systems green.")


my_order = Order("TXN_9982", "Credit Card", "FedEx")
my_order.finalize_order(250.75, "123 Maple Street, NY")
