"""Create a base class Shape with draw(). Derive Circle, Square, and Triangle. Select objects at runtime and call draw() polymorphically."""
class Shape2:
    def draw(self):
        raise NotImplementedError("Subclass must implement draw()")

class Circle2(Shape2):
    def draw(self):
        print("Drawing Circle")

class Square2(Shape2):
    def draw(self):
        print("Drawing Square")

class Triangle2(Shape2):
    def draw(self):
        print("Drawing Triangle")

def get_shape(choice: str) -> Shape2:
    choice = choice.lower()
    if choice == "circle":
        return Circle2()
    elif choice == "square":
        return Square2()
    elif choice == "triangle":
        return Triangle2()
    else:
        raise ValueError("Unknown shape")

# runtime selection
user_choices = ["circle", "square", "triangle"]

for ch in user_choices:
    shape_obj = get_shape(ch)   # object decided at runtime
    shape_obj.draw()
