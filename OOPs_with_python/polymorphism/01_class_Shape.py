"""
Create a base class Shape with area(). Derive Circle, Rectangle, and Triangle. 
Store different objects in a list and display their areas using a single loop.
"""
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

for s in shapes:          # single loop, polymorphic call
    print(type(s).__name__, "area:", s.area())
