"""5. Menu-Driven Shape Area Calculator
Create a base class Shape.
Derived classes: Circle, Rectangle, Triangle.
Menu options:
1. Choose shape
2. Calculate area
3. Exit
"""

import math


class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        # Placeholder method to be overridden by child classes
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius**2)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


def shape_menu():
    selected_shape = None

    while True:
        print("\n--- Shape Area Calculator ---")
        print("1. Choose Shape")
        print("2. Calculate Area")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            print("\nSelect Shape: 1. Circle | 2. Rectangle | 3. Triangle")
            s_type = input("Choice: ")

            if s_type == "1":
                r = float(input("Enter radius: "))
                selected_shape = Circle(r)
            elif s_type == "2":
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                selected_shape = Rectangle(l, w)
            elif s_type == "3":
                b = float(input("Enter base: "))
                h = float(input("Enter height: "))
                selected_shape = Triangle(b, h)
            else:
                print("Invalid shape selection.")
                continue

            print(f"{selected_shape.name} has been set!")

        elif choice == "2":
            if selected_shape:
                area = selected_shape.calculate_area()
                print(f"\nThe area of the {selected_shape.name} is: {area:.2f}")
            else:
                print("\nError: Please choose a shape first.")

        elif choice == "3":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    shape_menu()
