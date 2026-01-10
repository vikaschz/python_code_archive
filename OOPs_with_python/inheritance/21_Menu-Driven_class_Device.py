"""6. Menu-Driven Device Controller
Create a base class Device.
Derived classes: Mobile, Laptop.
Menu options:
1. Power ON
2. Power OFF
3. Exit
"""


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.brand} {self.model} is now powering ON..."
        return f"{self.brand} {self.model} is already ON."

    def power_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.brand} {self.model} is shutting down..."
        return f"{self.brand} {self.model} is already OFF."


# Derived classes inheriting from Device
class Mobile(Device):
    def power_on(self):
        # Specific behavior for Mobile
        base_msg = super().power_on()
        return f"{base_msg}\n[Screen showing Battery % and Signal Strength]"


class Laptop(Device):
    def power_on(self):
        # Specific behavior for Laptop
        base_msg = super().power_on()
        return f"{base_msg}\n[System checking RAM and loading OS...]"


def controller_menu():
    print("--- Device Setup ---")
    print("1. Mobile | 2. Laptop")
    choice = input("Select device to control: ")
    brand = input("Enter Brand: ")
    model = input("Enter Model: ")

    if choice == "1":
        my_device = Mobile(brand, model)
    else:
        my_device = Laptop(brand, model)

    while True:
        print(f"\n--- {my_device.brand} {my_device.model} Controller ---")
        print(f"Status: {'ON' if my_device.is_on else 'OFF'}")
        print("1. Power ON")
        print("2. Power OFF")
        print("3. Exit")

        option = input("Selection: ")

        if option == "1":
            print(my_device.power_on())
        elif option == "2":
            print(my_device.power_off())
        elif option == "3":
            print("Disconnecting device...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    controller_menu()
