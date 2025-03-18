#File for the managing of characters

#Imports needed csv library
import csv

#Big function to manage most of the character actions
def character_manager():
    #Opens the character file for all the inner functions
    with open('battle_simulator/character_stats.csv', 'a+') as file:
        #Saves a reader and writer
        writer = csv.writer(file)
        reader = csv.DictReader(file)

        #Function creates a character and adds it to the CSV
        def create_character(name, health, strength, defense, speed, level):
            #Make sure all stats are numbers, save int version into a lsit
            try:
                intStats = [int(health), int(strength), int(defense), int(speed)]
            except:
                print("One of your stats is not a number")
                return
            
            #Check if stat total is below limit and over min
            if intStats[0] + intStats[1] + intStats[2] + intStats[3] <= 800 and intStats[0] + intStats[1] + intStats[2] + intStats[3] >= 10:
                writer.writerow([name, health, strength, defense, speed, level])
                print("Character successfully created!")
            else:
                print("Your stat total is over the limit of 800 or under the limit of 10!")

            

        #Function that prints either all or one specific character
        def print_character(name):
            file.seek(0)

            #If they left blank, print all characters
            if name == "":
                next(reader)
                for i in reader:
                    print(i)
            else:
                #Prints character when found and switches a bool to signify
                found = False
                for i in reader:
                    if i['name'].upper() == name:
                        print(i)
                        found = True

                #If CSV fully read and bool is not switched, print error
                if not found:
                    print("The character was not found, feel free to create one with the name!")

        #Question based on what you do
        whatToDo = input("Would you like to create a new character (1), or see character (2)? ")
        
        #Calls inner helper function or error massage based on choice
        if whatToDo == "1":
            create_character(input("Character name: ").upper(), input("Health stat: "), input("Strength stat: "), input("Defense stat: "), input("Speed stat: "), input("Current level: "))
        elif whatToDo == "2":
            print_character(input("Enter character name to view (leave blank to print all): ").upper())
        else:
            print("Invalid choice.")