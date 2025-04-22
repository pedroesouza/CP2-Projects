#File for managing the csv (loading and adding things to it)

#Import needed library
import pandas as pd

#Import needed classes from other files
from shape import Circle, Square, Rectangle, Triangle

#Path to the shape's csv
csvPath = "geometry_calc/shapes.csv"

#This function reads all the shapes from the CSV
def load_shapes(shapes):
    csvShapes = pd.read_csv(csvPath)
    for i, row in csvShapes.iterrows():
        shape_type = str(row['type']).strip().lower()
        name = str(row['name']).strip().lower()
        if shape_type == 'circle':
            shapes.append(Circle(name, float(row['radius'])))
        elif shape_type == 'square':
            shapes.append(Square(name, float(row['length'])))
        elif shape_type == 'rectangle':
            shapes.append(Rectangle(name, float(row['length']), float(row['width'])))
        elif shape_type == 'triangle':
            shapes.append(Triangle(name, float(row['side1']), float(row['side2']), float(row['side3']), float(row['height'])))

#This function saves all shapes to the CSV
def save_shapes(shapes):
    data = []
    for shape in shapes:
        side1 = None
        side2 = None
        side3 = None
        length = None
        width = None
        radius = None
        height = None
        shape_type = type(shape).__name__.lower()
        if shape_type == 'circle':
            radius = shape.radius
        elif shape_type == 'square':
            length = shape.length
        elif shape_type == 'rectangle':
            length = shape.length
            width = shape.width
        elif shape_type == 'triangle':
            side1 = shape.side1
            side2 = shape.side2
            side3 = shape.side3
            height = shape.height

        data.append({
            'type': shape_type,
            'name': shape.name,
            'length': length,
            'width': width,
            'radius': radius,
            'side1': side1,
            'side2': side2,
            'side3': side3,
            'height': height
        })
    csvShapes = pd.DataFrame(data)
    csvShapes.to_csv(csvPath, index=False)
