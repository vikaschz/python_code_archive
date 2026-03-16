"""Create a base class Device with power(). Derive Mobile, Laptop, and Tablet. Toggle power using polymorphism."""
class Device:
    def power(self, on: bool):
        raise NotImplementedError("Subclass must implement power()")

class Mobile(Device):
    def power(self, on: bool):
        print("Mobile", "ON" if on else "OFF")

class Laptop(Device):
    def power(self, on: bool):
        print("Laptop", "ON" if on else "OFF")

class Tablet(Device):
    def power(self, on: bool):
        print("Tablet", "ON" if on else "OFF")

def toggle_power(device: Device, on: bool):
    device.power(on)

d: Device

d = Mobile()
toggle_power(d, True)

d = Laptop()
toggle_power(d, False)

d = Tablet()
toggle_power(d, True)
