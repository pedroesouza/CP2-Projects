#File for managing the csv (loading and adding things to it)

#Import needed library
import pandas as pd

#Import needed classes from other
from shape import Circle, Square, Rectangle, Triangle

#Path to the shape's csv
csvPath = "geometry_calc/shapes.csv"

#This funciton goes though the CSV and converts everything into objects
def load_shapes(shapes):
    csvShapes = pd.read_csv(csvPath) #using pandas to read the csv
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
            shapes.append(Triangle(name, float(row['base']), float(row['height'])))

#This puts all of the data in the CSV
def save_shapes(shapes):
    data = []
    for shape in shapes: #Loops though every shape to save them
        base = None
        height = None
        length = None
        width = None
        radius = None
        shape_type = type(shape).__name__.lower()
        if shape_type == 'circle':
            radius = shape.radius
        elif shape_type == 'square':
            length = shape.length
        elif shape_type == 'rectangle':
            length = shape.length
            width = shape.width
        elif shape_type == 'triangle':
            base = shape.base
            height = shape.height

        data.append({
            'type': shape_type,
            'name': shape.name,
            'length': length,
            'width': width,
            'radius': radius,
            'base': base,
            'height': height
        })
    csvShapes = pd.DataFrame(data)
    csvShapes.to_csv(csvPath, index=False)
