#Import needed library
import math

#Major class for all of the shapes with the name, area and perimeter since all shapes have that
class Shape:
    def __init__(self, name):
        self.name = name.lower()

    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        pass

#Circle subclass with specific formulas and radius
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def display(self):
        print(f"Circle '{self.name}': radius={self.radius}, diameter={2*self.radius}, area={self.area()}, perimeter={self.perimeter()}")

#Rectangle subclass with specific formulas length, and width
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return round(self.length * self.width, 2)

    def perimeter(self):
        return round(2 * (self.length + self.width), 2)

    def display(self):
        print(f"Rectangle '{self.name}': length={self.length}, width={self.width}, area={self.area()}, perimeter={self.perimeter()}")

#Square subclass of the rectangle subclass with specific formulas and all sides are the same size
class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)

    def display(self):
        print(f"Square '{self.name}': side={self.length}, area={self.area()}, perimeter={self.perimeter()}")

#Triangle subclass with specific formulas, base and height
class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return round(0.5 * self.base * self.height, 2)

    def perimeter(self):
        return None  # Not enough info for perimeter

    def display(self):
        print(f"Triangle '{self.name}': base={self.base}, height={self.height}, area={self.area()}, perimeter=N/A")
