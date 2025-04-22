#Function for the classes so that they can be created abotu objects

#Import needed library
import math

#Major class for all of the shapes with the name, area and perimeter since all shapes have that
class Shape:
    def __init__(self, name):
        self.name = name.lower()

    #Function to calculate area
    def area(self):
        pass

    #Function to calculate perimeter
    def perimeter(self):
        pass

    #Function to display the shape
    def display(self):
        pass

#Circle subclass with specific formulas and radius
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    #Area of circle = pi * radius^2
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    #Perimeter of circle = 2 * pi * radius
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    #Display the circle's data
    def display(self):
        print(f"Circle '{self.name}': radius={self.radius}, diameter={2*self.radius}, area={self.area()}, perimeter={self.perimeter()}")

#Rectangle subclass with specific formulas length, and width
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    #Area of rectangle = length * width
    def area(self):
        return round(self.length * self.width, 2)

    #Perimeter of rectangle = 2 * (length + width)
    def perimeter(self):
        return round(2 * (self.length + self.width), 2)

    #Display the rectangle's data
    def display(self):
        print(f"Rectangle '{self.name}': length={self.length}, width={self.width}, area={self.area()}, perimeter={self.perimeter()}")

#Square subclass of the rectangle subclass with specific formulas and all sides are the same size
class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)

    #Display the square's data
    def display(self):
        print(f"Square '{self.name}': side={self.length}, area={self.area()}, perimeter={self.perimeter()}")

#Triangle subclass with specific formulas, sides and height
class Triangle(Shape):
    def __init__(self, name, side1, side2, side3, height):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height

    #Area of triangle = 0.5 * base * height (using side1 as the base)
    def area(self):
        return round(0.5 * self.side1 * self.height, 2)

    #Perimeter of triangle = side1 + side2 + side3
    def perimeter(self):
        return round(self.side1 + self.side2 + self.side3, 2)

    #Display the triangle's data
    def display(self):
        print(f"Triangle '{self.name}': sides=({self.side1}, {self.side2}, {self.side3}), height={self.height}, area={self.area()}, perimeter={self.perimeter()}")
