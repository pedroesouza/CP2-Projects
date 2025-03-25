#Imports needed csv library
import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt

fake = Faker('en_US')

#Big function to manage most of the character actions
def character_manager():
    reader = pd.read_csv('battle_simulator/character_stats.csv')

    #Function creates a character and adds it to the CSV
    def create_character(name, health, strength, defense, speed, level):
        #Make sure all stats are numbers, save int version into a list
        try:
            intStats = [int(health), int(strength), int(defense), int(speed)]
        except:
            print("One of your stats is not a number")
            return

        #Check if stat total is below limit and over min to save
        if sum(intStats) <= 800 and sum(intStats) >= 10:
            new_character = pd.DataFrame([{
                "name": name,
                "health": health,
                "strength": strength,
                "defense": defense,
                "speed": speed,
                "level": level,
                "description": f"{name} is from {fake.city()} and is a(n) {fake.job()}" #generate backstory with faker
            }])
            reader_updated = pd.concat([reader, new_character], ignore_index=True)
            reader_updated.to_csv("battle_simulator/character_stats.csv", index=False)
            print("Character successfully created!")
        else:
            print("Your stat total is over the limit of 800 or under the limit of 10!")

    #Function that prints either all or one specific character
    def print_character(name):
        #If they left blank, print all characters
        if name == "":
            print(reader.to_string(index=False))
        else:
            #Prints character when found
            found = reader[reader["name"].str.upper() == name]
            if not found.empty:
                print(found.to_string(index=False))
                
                #Extract stats for the character (excluding level)
                stats = found[['health', 'strength', 'defense', 'speed']].iloc[0]
                
                #Calculate the min, max, and avg of the stats
                minStat = stats.min()
                maxStat = stats.max()
                avgStat = stats.mean()
                
                #Print stuff in terminal
                print(f"\nStats Summary for {name}:")
                print(f"Minimum Stat: {minStat}")
                print(f"Maximum Stat: {maxStat}")
                print(f"Mean Stat: {avgStat:.2f}")

                plt.figure(figsize=(8, 6))

                #Plot the character stats
                plt.bar(stats.index, stats.values, color='lightcoral', label='Character Stats')
                
                #Add the min, max, and average as side lines on the graph
                plt.axhline(minStat, color='blue', linestyle='--', label=f'Min: {minStat}')
                plt.axhline(maxStat, color='green', linestyle='--', label=f'Max: {maxStat}')
                plt.axhline(avgStat, color='orange', linestyle='--', label=f'Mean: {avgStat:.2f}')
                
                #Set labels and title
                plt.title(f"Stats for {name}")
                plt.xlabel("Stat")
                plt.ylabel("Value")
                plt.legend(loc='upper left')
                
                #Save the plot as an image file
                plt.savefig(f'{name}_stats.png')
                print(f"Plot for {name} saved as '{name}_stats.png'.")
                
                #Show the plot (this may not show in Codespace, but it will save as a file)
                plt.show()
                plt.close()
            else:
                print("The character was not found, feel free to create one with the name!")

    def mean_of_chars():
        #Finds all of lines and stats that have numbers in them
        numOfCharacters = reader.select_dtypes(include='number')
        
        #Use .mean (really useful haha) to calculate the mean of stats
        meanOfStats = numOfCharacters.mean()
        
        print("Average Character Stats:")
        for stat, value in meanOfStats.items():
            print(f"{stat}: {value:.2f}")
        
        #Plotting the average character between all characters in a bar graph
        plt.figure(figsize=(8, 6))
        plt.bar(meanOfStats.index, meanOfStats.values, color='skyblue')
        plt.title("Average Character Stats")
        plt.xlabel("Stat")
        plt.ylabel("Average Value")
        
        plt.savefig('average_stats.png')  #Save the plot as an image file for codespaces
        print("Plot saved as 'average_stats.png'.")
        
        #Show the plot (this might not show in Codespace, but it will save as a file)
        plt.show()
        plt.close()

    #Question based on what you do
    whatToDo = input("Would you like to create a new character (1), see character or characters (2), see character average scores (3)? ")
    
    #Calls inner helper function or error message based on choice
    if whatToDo == "1":
                        #(below ;)Name is now rardom
        create_character(fake.name().upper(), input("Health stat: "), input("Strength stat: "), input("Defense stat: "), input("Speed stat: "), input("Current level: "))
    elif whatToDo == "2":
        print_character(input("Enter character name to view, note: the description is printed on the terminal (leave blank to print all [no graph]): ").upper())
    elif whatToDo == "3":
        mean_of_chars()
    else:
        print("Invalid choice.") #Idiot proofing
