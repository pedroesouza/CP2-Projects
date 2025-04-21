#Sorts shapes in specific category in order or perimiter or area

#Function that asks for the criteria and category and then sorts it from higherst criteria to lowest
def sort_shapes(shapes):
    #Asks user for criteria and filter
    criteria = input("Sort by area or perimeter: ").strip().lower()
    filterType = input("Enter shape type to filter or 'all': ").strip().lower()

    #Idiot proofing error managing
    if criteria not in ["area", "perimeter"]:
        print("Invalid, please only select area or perimeter.")
        return
    if filterType not in ["all", "circle", "triangle", "rectangle", "square"]:
        print("Invalid filter")
        return
    
    #Find and sorts the shapes
    filtered = shapes if filterType == "all" else [s for s in shapes if type(s).__name__.lower() == filterType]
    try:
        if criteria == "area":
            sorted_shapes = sorted(filtered, key=lambda x: x.area())
        else:
            sorted_shapes = sorted(filtered, key=lambda x: x.perimeter() if x.perimeter() is not None else -1)
        for shape in sorted_shapes:
            shape.display()
    except:
        print("Error sorting shapes.")
