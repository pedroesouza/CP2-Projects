#Pedro Souza, Classes Project

#Main function for asking for choice and calling other functions 

#Import all classes, functions and things from other files that are needed
from shape import Circle, Square, Rectangle, Triangle
from csv_manager import load_shapes
from shape_creator import create_shape
from shape_viewer import see_shapes
from shape_comparer import compare_shapes
from shape_sorter import sort_shapes
from shape_deleter import delete_shape

#The main function thats going to handle all the asking and calling for the user
def main():
    shapes = [] #Creates the basic list for all the shapes
    load_shapes(shapes) #Loads the shapes from the CSV to the list
    while True: #Loops until the program is exited

        #Asks user what they want to do and calls right function based on choice
        print("""
1. Create Shape
2. See Shapes
3. Compare Shapes
4. Sort Shapes
5. Delete Shape
6. Exit""") 
        choice = input("Choose an option: ").strip()
        if choice == '1':
            create_shape(shapes)
        elif choice == '2':
            see_shapes(shapes)
        elif choice == '3':
            compare_shapes(shapes)
        elif choice == '4':
            sort_shapes(shapes)
        elif choice == '5':
            delete_shape(shapes)
        elif choice == '6':
            break
        else: #Error managing
            print("Invalid option.")

#First main call that kickstarts everything
main()
