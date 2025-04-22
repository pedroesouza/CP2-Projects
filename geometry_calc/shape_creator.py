#Shape creator file that saves and creates the shapes using their classes

#Import needed classes and files
from shape import Circle, Square, Rectangle, Triangle
from csv_manager import save_shapes

#Function creates the shape and sets up CSV manager to save it
def create_shape(shapes):
    #Asks for name and shape type, making sure that the name is unique
    shape_type = input("Enter shape type (circle/square/rectangle/triangle): ").strip().lower()
    name = input("Enter a unique name for the shape: ").strip().lower()
    if any(s.name == name for s in shapes):
        print("A shape with this name already exists.")
        return
    try:
        #Ask user for info on the shape
        if shape_type == 'circle':
            radius = float(input("Enter radius: "))
            if radius > 0:
                shapes.append(Circle(name, radius))
            else:
                print("No negatives or zero's allowed")
        elif shape_type == 'square':
            side = float(input("Enter side length: "))
            if side > 0:
                shapes.append(Square(name, side))
            else:
                print("No negatives or zero's allowed")
        elif shape_type == 'rectangle':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            if length > 0 and width > 0:
                shapes.append(Rectangle(name, length, width))
            else:
                print("No negatives or zero's allowed")
        elif shape_type == 'triangle':
            side1 = float(input("Enter side 1 length: "))
            side2 = float(input("Enter side 2 length: "))
            side3 = float(input("Enter side 3 length: "))
            height = float(input("Enter height: "))
            if side1 > 0 and side2 > 0 and side3 > 0 and height > 0:
                shapes.append(Triangle(name, side1, side2, side3, height))
            else:
                print("No negatives or zero's allowed")
        else:
            print("Invalid shape type.")
            return
        save_shapes(shapes)  #Save the new shapes to CSV
        print("Shape created successfully.")
    except:
        print("Invalid answer, not a number.")  #Handle invalid input
