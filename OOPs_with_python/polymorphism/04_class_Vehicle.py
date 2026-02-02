"""Create a base class Vehicle with start() and stop(). Derive Car, Bike, and Bus. Use a single reference variable to control different vehicles."""
class Vehicle:
    def start(self):
        raise NotImplementedError("Subclass must implement start()")

    def stop(self):
        raise NotImplementedError("Subclass must implement stop()")

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")

v: Vehicle  # single reference

v = Car()
v.start()
v.stop()

v = Bike()
v.start()
v.stop()

v = Bus()
v.start()
v.stop()
