#File for managing all that happens in the actual battles

#Imports necessary files
import csv
import random

#Big function for managing all the inner functions on the battle, it starts it off by calling the character choice function
def battle_main():
    #For chosing characters, it asks, looks for, saves, formats, and returns the character's dictionaries to be use
    def chose_characters(charOne, charTwo):
        with open('battle_simulator/character_stats.csv', 'r') as file:
            reader = csv.DictReader(file)
            funcCharOneDict = {}
            funcCharTwoDict = {}
            for i in reader:
                char_name = i['name'].strip().upper()
            
                if char_name == charOne:
                    funcCharOneDict = {k.strip().lower(): v.strip() for k, v in i.items()}
                elif char_name == charTwo:
                    funcCharTwoDict = {k.strip().lower(): v.strip() for k, v in i.items()}
        
        return funcCharOneDict, funcCharTwoDict

    #Calls the chose function
    charOneDict, charTwoDict = chose_characters(input("What is the name of player 1's character? ").strip().upper(), input("What is the name of player 2's character? ").strip().upper())

    #Gives error if one of the dictionaries is blank (meaning charcter was not in list)
    if not charOneDict or not charTwoDict:
        print("One or both characters not found.")
        return

    #Uses a simple formatting to convery what each play did
    def print_player_move(num, otherNum, move, enemyHP):
        print(f"Player {num} used {move}")
        print(f"Player {otherNum}'s health is now {enemyHP}")

    #Function ends game, by announcing a battle is over, the winner and going though the dictionary to level up the winner
    def end_game():
        print("Battle over!")
        playerOneHealth = int(charOneDict["health"].strip())

        #Checks for winner to announce and adds level to winner
        if playerOneHealth <= 0:
            print("Player 2 wins!")
            charTwoDict["level"] = str(int(charTwoDict["level"]) + 1)
        else:
            print("Player 1 wins!")
            charOneDict["level"] = str(int(charOneDict["level"]) + 1)

        #Saves dictionary reader for uses in the level up
        with open('battle_simulator/character_stats.csv', 'r') as file:
            reader = list(csv.DictReader(file))
        
        #Revwries the level, and only the level of the winner on the csv with one more stat
        keyNames = ["name", "health", "strength", "defense", "speed", "level"]
        with open('battle_simulator/character_stats.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keyNames)
            writer.writeheader()
            for row in reader:
                if row['name'].strip().upper() == charOneDict['name'].upper():
                    row["level"] = charOneDict["level"]
                elif row['name'].strip().upper() == charTwoDict['name'].upper():
                    row["level"] = charTwoDict["level"]
                writer.writerow(row)

    #Simple function that runs the damage formula off of the player dictionaries and returns it
    def damage_calculator(attacker, defender, base_damage):
        attack = int(attacker.get("strength"))
        defense = int(defender.get("defense"))
        level_attacker = int(attacker.get("level"))
        level_defender = int(defender.get("level"))
        
        damage = base_damage * ((attack * (1 + (level_attacker / 75))) / (defense * (1 + (level_defender / 75))))
        return max(1, round(damage))

    #THe big chunky function that checks the player combination of choice and speed to run the correct turn
    def player_choice():
        #Runs the game while no one is dead
        while int(charOneDict.get("health", 0)) > 0 and int(charTwoDict.get("health", 0)) > 0:
            #Asking the players for their moves one at a time
            print("Player 1 turn")
            moveOne = input("Would you like to heavy attack (1), quick attack (2), or defend (3)? ")
            print("Player 2 turn")
            moveTwo = input("Would you like to heavy attack (1), quick attack (2), or defend (3)? ")
          
            #Sees what combination the player chose and runs the correct turn for it          
            if moveOne in ["1", "2", "3"] and moveTwo in ["1", "2", "3"]: #Just makes sure there are no invalid inputs (its else just gives an error)
                if moveOne == "1": 
                    if moveTwo == "1":  
                        if charOneDict["speed"] > charTwoDict["speed"]:
                            charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 50))
                            print_player_move("one", "two", "heavy attack", charTwoDict["health"])
                            charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 50))
                            print_player_move("two", "one", "heavy attack", charOneDict["health"])
                        elif charOneDict["speed"] < charTwoDict["speed"]:
                            charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 50))
                            print_player_move("two", "one", "heavy attack", charOneDict["health"])
                            charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 50))
                            print_player_move("one", "two", "heavy attack", charTwoDict["health"])
                        else:
                            if random.choice([1, 2]) == 1:
                                charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 50))
                                print_player_move("two", "one", "heavy attack", charOneDict["health"])
                                charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 50))
                                print_player_move("one", "two", "heavy attack", charTwoDict["health"])
                            else:
                                charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 50))
                                print_player_move("one", "two", "heavy attack", charTwoDict["health"])
                                charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 50))
                                print_player_move("two", "one", "heavy attack", charOneDict["health"])

                    elif moveTwo == "2":  
                        charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 35))
                        print_player_move("two", "one", "quick attack", charOneDict["health"])
                        charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 50))
                        print_player_move("one", "two", "heavy attack", charTwoDict["health"])

                    elif moveTwo == "3": 
                        charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charOneDict, 25))
                        print("Player two protected, but player one's move broke through it and deals partial damage!")
                        print_player_move("one", "two", "protected heavy attack", charTwoDict["health"])

                elif moveOne == "2": 
                    if moveTwo == "1":  
                        charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 35))
                        print_player_move("one", "two", "quick attack", charTwoDict["health"])
                        charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 50))
                        print_player_move("two", "one", "heavy attack", charOneDict["health"])

                    elif moveTwo == "2": 
                        if charOneDict["speed"] > charTwoDict["speed"]:
                            charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 35))
                            print_player_move("one", "two", "quick attack", charTwoDict["health"])
                            charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 35))
                            print_player_move("two", "one", "quick attack", charOneDict["health"])
                        elif charOneDict["speed"] < charTwoDict["speed"]:
                            charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 35))
                            print_player_move("two", "one", "quick attack", charOneDict["health"])
                            charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 35))
                            print_player_move("one", "two", "quick attack", charTwoDict["health"])
                        else:
                            if random.choice([1, 2]) == 1:
                                charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 35))
                                print_player_move("two", "one", "quick attack", charOneDict["health"])
                                charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charOneDict, 35))
                                print_player_move("one", "two", "quick attack", charTwoDict["health"])
                            else:
                                charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charOneDict, 35))
                                print_player_move("one", "two", "quick attack", charTwoDict["health"])
                                charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 35))
                                print_player_move("two", "one", "quick attack", charOneDict["health"])

                    elif moveTwo == "3":  
                        charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charOneDict, charOneDict, 40))
                        print("Player one uses a quick attack, but player two protects and player one hurts themself!")
                        print(f"Player one is now at {charOneDict['health']} HP")

                elif moveOne == "3": 
                    if moveTwo == "1": 
                        charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 25))
                        print("Player one protected, but player two's move broke through it and deals partial damage!")
                        print_player_move("two", "one", "protected heavy attack", charOneDict["health"])
                    elif moveTwo == "2": 
                        charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charTwoDict, charTwoDict, 40))
                        print("Player two uses a quick attack, but player one protects and player one hurts themself!")
                        print(f"Player two is now at {charTwoDict['health']} HP")
                    elif moveTwo == "3":
                        print("Both protected, nothing happened")
            else:
                print("Invalid move selection")
        end_game()

    player_choice()