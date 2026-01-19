"""Create a base class Animal with sound(). Derive Dog, Cat, and Cow. Write a function that accepts an Animal reference and calls sound() polymorphically."""
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement sound()")

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

def make_sound(animal: Animal):
    # runtime polymorphism: which sound() runs depends on object type
    print(type(animal).__name__, "sound:", animal.sound())

animals = [Dog(), Cat(), Cow()]

for a in animals:
    make_sound(a)
