#Shape creator file that saves and creates the shapes using their classes

#Import needed classes and files
from shape import Circle, Square, Rectangle, Triangle
from csv_manager import save_shapes

#Function creates the shape and sets up csv manager to save it
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
            if radius > 0: #This and others like this just make sure the number is valid
                shapes.append(Circle(name, radius))
            else:
                print("No negatives or zero's allowed")
        elif shape_type == 'square':
            side = float(input("Enter side length: "))
            if radius > 0:
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
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            if base > 0 and height > 0:
                shapes.append(Triangle(name, base, height))
            else:
                print("No negatives or zero's allowed")
        else: #Error managing idiot proofing
            print("Invalid shape type.")
            return
        save_shapes(shapes) #call the function to save the shapes on csv
        print("Shape created successfully.")
    except:
        print("Invalid answer, not a number.") #For when the number is not a number
