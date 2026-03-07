"""Create a base class Appliance with operate(). Derive Fan, Light, and AC. Change objects at runtime and call operate() without modifying calling code."""
class Appliance:
    def operate(self):
        raise NotImplementedError("Subclass must implement operate()")

class Fan(Appliance):
    def operate(self):
        print("Fan is rotating")

class Light(Appliance):
    def operate(self):
        print("Light is glowing")

class AC(Appliance):
    def operate(self):
        print("AC is cooling")

def run_appliance(appliance: Appliance):
    appliance.operating_mode = "ON"   # dynamic attribute, still polymorphic call
    appliance.operate()

appliance: Appliance

appliance = Fan()
run_appliance(appliance)

appliance = Light()
run_appliance(appliance)

appliance = AC()
run_appliance(appliance)
