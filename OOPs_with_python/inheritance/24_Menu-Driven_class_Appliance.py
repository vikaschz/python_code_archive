"""9. Menu-Driven Appliance Controller
Create a base class Appliance.
Derived classes: Fan, Light, AC.
Menu options:
1. Choose appliance
2. Operate appliance
3. Exit
"""


class Appliance:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return f"{self.name} is now ON."

    def operate(self):
        # To be overridden by subclasses
        pass


class Fan(Appliance):
    def operate(self):
        if self.is_on:
            return f"🌀 The {self.name} is spinning at medium speed."
        return f"❌ Cannot operate. The {self.name} is OFF."


class Light(Appliance):
    def operate(self):
        if self.is_on:
            return f"💡 The {self.name} is illuminating the room at 100% brightness."
        return f"❌ Cannot operate. The {self.name} is OFF."


class AC(Appliance):
    def operate(self):
        if self.is_on:
            return f"❄️ The {self.name} is cooling the room to 22°C."
        return f"❌ Cannot operate. The {self.name} is OFF."


def appliance_menu():
    current_appliance = None

    while True:
        print("\n--- Smart Home Appliance Controller ---")
        print("1. Choose Appliance")
        print("2. Operate Appliance")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            print("\nSelect Type: 1. Fan | 2. Light | 3. AC")
            type_choice = input("Choice: ")
            room = input("Enter room location (e.g., Bedroom): ")

            if type_choice == "1":
                current_appliance = Fan(f"Fan ({room})")
            elif type_choice == "2":
                current_appliance = Light(f"Light ({room})")
            elif type_choice == "3":
                current_appliance = AC(f"AC ({room})")
            else:
                print("Invalid selection.")
                continue

            # Automatically turn it on for this demonstration
            print(current_appliance.turn_on())

        elif choice == "2":
            if current_appliance:
                print("\n" + current_appliance.operate())
            else:
                print("\nError: Please select an appliance first (Option 1).")

        elif choice == "3":
            print("Shutting down controller. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    appliance_menu()
