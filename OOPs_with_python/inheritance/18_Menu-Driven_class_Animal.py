"""3. Menu-Driven Animal Sound System
Create a base class Animal with sound().
Derived classes: Dog, Cat, Cow (override sound()).
Menu options:
1. Choose animal
2. Produce sound
3. Exit
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "The animal makes a generic sound."


# Hierarchical Inheritance: Multiple subclasses inheriting from 'Animal'
class Dog(Animal):
    def sound(self):
        return f"{self.name} says: Woof! Woof!"


class Cat(Animal):
    def sound(self):
        return f"{self.name} says: Meow! Meow!"


class Cow(Animal):
    def sound(self):
        return f"{self.name} says: Moo! Moo!"


def animal_menu():
    selected_animal = None

    while True:
        print("\n--- Animal Sound System ---")
        print("1. Choose Animal")
        print("2. Produce Sound")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            print("\nSelect Animal Type: 1. Dog | 2. Cat | 3. Cow")
            a_type = input("Choice: ")
            name = input("Enter a name for your animal: ")

            if a_type == "1":
                selected_animal = Dog(name)
            elif a_type == "2":
                selected_animal = Cat(name)
            elif a_type == "3":
                selected_animal = Cow(name)
            else:
                print("Invalid animal type selected.")
                continue

            print(f"Success! {name} the {type(selected_animal).__name__} is ready.")

        elif choice == "2":
            if selected_animal:
                print("\n" + selected_animal.sound())
            else:
                print("\nError: Please choose an animal first (Option 1).")

        elif choice == "3":
            print("Closing system. Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    animal_menu()
