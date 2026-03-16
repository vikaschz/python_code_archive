"""Create a base class GameCharacter with attack(). Derive Warrior, Archer, and Mage. Store objects in a list and invoke attack()."""
class GameCharacter:
    def __init__(self, name):
        self.name = name

    def attack(self):
        raise NotImplementedError("Subclass must implement attack()")

class Warrior(GameCharacter):
    def attack(self):
        print(self.name, "swings a sword")

class Archer(GameCharacter):
    def attack(self):
        print(self.name, "shoots an arrow")

class Mage(GameCharacter):
    def attack(self):
        print(self.name, "casts a spell")

characters = [
    
    Warrior("Thor"),
    Archer("Legolas"),
    Mage("Gandalf")
]

for c in characters:
    c.attack()