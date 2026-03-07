"""Create a base class Transport with fare(). Derive Bus, Train, and Flight. Calculate fare polymorphically."""
class Transport:
    def fare(self, distance_km):
        raise NotImplementedError("Subclass must implement fare()")

class Bus(Transport):
    def fare(self, distance_km):
        return distance_km * 5  # simple per km

class Train(Transport):
    def fare(self, distance_km):
        return distance_km * 3 + 50  # base + per km

class Flight(Transport):
    def fare(self, distance_km):
        return distance_km * 10 + 500  # premium

def print_fare(t: Transport, distance_km):
    print(type(t).__name__, "fare:", t.fare(distance_km))

modes = [Bus(), Train(), Flight()]

for m in modes:
    print_fare(m, 100)
