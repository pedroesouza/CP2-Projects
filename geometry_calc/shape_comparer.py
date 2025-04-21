#Comparer function so that you can compare two shapes by either area or perimeter

#Function that does the comparer depending on user choice of parameter and shapes
def compare_shapes(shapes):
    #Searches for the names, asks for what they want to compare
    name1 = input("Enter first shape name: ").strip().lower()
    name2 = input("Enter second shape name: ").strip().lower()
    criteria = input("Compare by 'area' or 'perimeter': ").strip().lower()
    shape1 = next((s for s in shapes if s.name == name1), None)
    shape2 = next((s for s in shapes if s.name == name2), None)

    if not shape1 or not shape2:
        print("One or both shapes not found.") #Error message for invalid shape
        return
    if criteria == 'area':
        val1, val2 = shape1.area(), shape2.area()
    elif criteria == 'perimeter':
        val1, val2 = shape1.perimeter(), shape2.perimeter()
        if val1 is None or val2 is None:
            print("One or both shapes do not have a defined perimeter.")
            return
    else:
        print("Invalid criteria.")
        return
    if val1 > val2:
        print(f"{shape1.name} has a larger {criteria}.")
    elif val1 < val2:
        print(f"{shape2.name} has a larger {criteria}.")
    else:
        print("Both shapes are equal in that criteria.")
