#Import csv so we can read the movies list later on
import csv

#This function uses the variables it is given to print specific movies that match them
def print_filtered(title, director, genre, rating, length, actor):
    with open("music_recommender\movies_list.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for currentMovie in reader: #Just loops through every movie to check if it fits the selected criteria
            if title in currentMovie[0].lower() and director in currentMovie[1].lower() and genre in currentMovie[2].lower() and rating in currentMovie[3].lower() and int(currentMovie[4]) + 7.5 >= length and int(currentMovie[4]) - 7.5 <= length and actor in currentMovie[5].lower():
              #This long thing is basically checking if the currentMovie that is being tested is following the parameters
                print(currentMovie) #The movie is printed if it follows it
        print("These movies match your requirements")

#Function that prints all of the movies in the list
def print_all():
    with open("music_recommender\movies_list.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for currentMovie in reader:
            print(currentMovie)

#This function asks and sets values for parameters, then runs print_filtered with the criteria as its variables
def set_parameter():
    #Resets variables
    title = ""
    director = ""
    genre = ""
    rating = ""
    length = 0
    actor = ""

  #Asks if the user whants to add/ change a parameter until the user decides to see the avaliable movies
    while True:
        requirementChoice = input("\nPlease select your next action\n1: Add title parameter\n2: Add director parameter\n3: Add genre parameter\n4: Add rating parameter\n5: Add length parameter\n6: Add actor parameter\n7: Find movies matching the criteria\n")
        
        if requirementChoice == "1":
            title = input("What is the title you are looking for: ").lower()
        elif requirementChoice == "2":
            director = input("Who is the director you are looking for: ").lower()
        elif requirementChoice == "3":
            genre = input("What is the genre you are looking for: ").lower()
        elif requirementChoice == "4":
            rating = input("What is the rating you are looking for: ").lower()
        elif requirementChoice == "5":
            try:
                length = int(input("What is the minimum length you want: "))
            except:
                print("Invalid length. Please enter a number.")
        elif requirementChoice == "6":
            actor = input("What is the actor you are looking for: ").lower()
        elif requirementChoice == "7":
            print_filtered(title, director, genre, rating, length, actor)
            break
        #Idiot proofing
        else:
            print("Invalid input, please only answer with numbers 1-7")

#Main function handles user choices
def main():
        #Question of what user wants to do
        actionChoice = input("\nPlease select your next action\n1: Display all movies\n2: Search for specific movies\n3: Exit the program\n")

        #Runs specific function or does something based on question answer
        if actionChoice == "1":
            print_all()
        elif actionChoice == "2":
            set_parameter()
        elif actionChoice == "3":
            exit()
        #Idiot proofing
        else:
            print("Invalid input, please only insert 1, 2, or 3")

#Run the main function in a loop
while True:
    main()
