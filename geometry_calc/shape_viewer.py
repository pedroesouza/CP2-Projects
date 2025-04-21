#Shape viwer file for searching and looking at all the shapes

#Function to view the shapes
def see_shapes(shapes):
    option = input("Enter shape name to search or type 'all': ").strip().lower() #asks user to either put a name or leave blank to see all shapes

    if option == 'all': #prints all
        for shape in shapes:
            shape.display()
    else:
        found = False
        for shape in shapes: #prints specific searched
            if shape.name == option:
                shape.display()
                found = True
        if not found:
            print("Shape not found.") #error managing idiot proofing
