#Shape deleter file, deletes shape

#Import needed library
from csv_manager import save_shapes

#This is pretty simple, it just deletes a shape if found
def delete_shape(shapes):
    name = input("Enter shape name to delete: ").strip().lower() #Ask
    new_shapes = [s for s in shapes if s.name != name] #The shapes without it
    if len(new_shapes) == len(shapes): #If the new and old are the same, there was no shape of that name
        print("Shape not found.")
    else:
        shapes = new_shapes
        save_shapes(shapes)
        print("Shape deleted.")
