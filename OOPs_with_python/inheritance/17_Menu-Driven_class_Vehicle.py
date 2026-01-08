"""
2. Menu-Driven Vehicle Control System
Create a base class Vehicle.
Derived classes: Car, Bike, Bus.
Demonstrate hierarchical inheritance.
Menu options:
1. Choose vehicle
2. Start vehicle
3. Stop vehicle
4. Exit
"""


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"The {self.brand} vehicle is starting..."

    def stop(self):
        return f"The {self.brand} vehicle has stopped."


class Car(Vehicle):
    def start(self):
        return f"Car ({self.brand}): Engine purring. Ready to drive."


class Bike(Vehicle):
    def start(self):
        return f"Bike ({self.brand}): Kickstart successful. Ready to ride."


class Bus(Vehicle):
    def start(self):
        return f"Bus ({self.brand}): Air brakes released. Ready for passengers."


def menu():
    current_vehicle = None

    while True:
        print("\n--- Vehicle Control System ---")
        print("1. Choose Vehicle")
        print("2. Start Vehicle")
        print("3. Stop Vehicle")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            print("\nSelect Type: 1. Car | 2. Bike | 3. Bus")
            v_type = input("Choice: ")
            brand = input("Enter Brand Name: ")

            if v_type == "1":
                current_vehicle = Car(brand)
            elif v_type == "2":
                current_vehicle = Bike(brand)
            elif v_type == "3":
                current_vehicle = Bus(brand)
            else:
                print("Invalid type selection.")

            if current_vehicle:
                print(f"{type(current_vehicle).__name__} selected!")

        elif choice == "2":
            if current_vehicle:
                print(current_vehicle.start())
            else:
                print("Please choose a vehicle first!")

        elif choice == "3":
            if current_vehicle:
                print(current_vehicle.stop())
            else:
                print("Please choose a vehicle first!")

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()
