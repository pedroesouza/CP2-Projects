import csv
import random
import os

def check_file(file):
    if os.path.exists(file):
        return False
    else:
        print("File does not exist")
        return True

def character_manager():
    filePath = input("What is the relative file path to your characters? ")
    if check_file(filePath):
        return
    
    with open(filePath, 'a+') as file:
        writer = csv.writer(file)
        reader = csv.DictReader(file)

        def create_character(name, health, strength, defense, speed, level):
            writer.writerow([name, health, strength, defense, speed, level])
            print("Character successfully created!")

        def print_character(name):
            file.seek(0)
            if name == "":
                next(reader)
                for i in reader:
                    print(i)
            else:
                found = False
                for i in reader:
                    if i['name'].upper() == name:
                        print(i)
                        found = True
                if not found:
                    print("The character was not found, feel free to create one with the name!")

        whatToDo = input("Would you like to create a new character (1), or see character (2)? ")
        if whatToDo == "1":
            create_character(
                input("Character name: ").upper(),
                input("Health stat: "),
                input("Strength stat: "),
                input("Defense stat: "),
                input("Speed stat: "),
                input("Current level: ")
            )
        elif whatToDo == "2":
            print_character(input("Enter character name to view (leave blank to print all): ").upper())

        else:
            print("Invalid choice.")

def battle_main():
    filePath = input("What is the relative file path to your characters? ")

    if check_file(filePath):
        return

    def chose_characters(charOne, charTwo):
        with open(filePath, 'r') as file:
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

    def damage_calculator(attacker, defender, base_damage):
        attack = int(attacker.get("strength", 0))
        defense = int(defender.get("defense", 1))
        return max(1, base_damage + ((attack - defense) // 2)+((level*0.25)*base_damage))

    charOneDict, charTwoDict = chose_characters(
        input("What is the name of player 1's character? ").strip().upper(),
        input("What is the name of player 2's character? ").strip().upper()
    )

    if not charOneDict or not charTwoDict:
        print("One or both characters not found.")
        return

    def print_player_move(num, otherNum, move, enemyHP):
        print(f"Player {num} used {move}")
        print(f"Player {otherNum}'s health is now {enemyHP}")


    def end_game():
        print("Battle over!")
        if int(charOneDict["health"]) <= 0:
            print("Player 2 wins!")
            charTwoDict["level"] = str(int(charTwoDict["level"]) + 1)
        else:
            print("Player 1 wins!")
            charOneDict["level"] = str(int(charOneDict["level"]) + 1)

        with open(filePath, 'r') as file:
            reader = list(csv.DictReader(file))
        
        fieldnames = ["name", "health", "strength", "defense", "speed", "level"]  # Ensure correct fields
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if row['name'].strip().upper() == charOneDict['name'].upper():
                    row["level"] = charOneDict["level"]
                elif row['name'].strip().upper() == charTwoDict['name'].upper():
                    row["level"] = charTwoDict["level"]
                writer.writerow(row)


    def player_choice():
        while int(charOneDict.get("health", 0)) > 0 and int(charTwoDict.get("health", 0)) > 0:
            print("Player 1 turn")
            moveOne = input("Would you like to heavy attack (1), quick attack (2), or defend (3)? ")
            print("Player 2 turn")
            moveTwo = input("Would you like to heavy attack (1), quick attack (2), or defend (3)? ")
            if moveOne in ["1", "2", "3"] and moveTwo in ["1", "2", "3"]:

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
                            if random.choice[1,2] == 1:
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
                        charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 25))
                        print("Player two protect, but player one's move broke through it and deals partial damage!")
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
                            if random.choice[1,2] == 1:
                                charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 35))
                                print_player_move("two", "one", "quick attack", charOneDict["health"])
                                charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 35))
                                print_player_move("one", "two", "quick attack", charTwoDict["health"])
                            else:
                                charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charOneDict, charTwoDict, 35))
                                print_player_move("one", "two", "quick attack", charTwoDict["health"])
                                charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 35))
                                print_player_move("two", "one", "quick attack", charOneDict["health"])

                    elif moveTwo == "3":
                        charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charOneDict, charOneDict, 40))
                        print("Player one uses a quick attack, but player two protects and player one hurts themself!")
                        print(f"Player one is now at {charOneDict["health"]} HP")

                elif moveOne == "3":
                    if moveTwo == "1":
                        charOneDict["health"] = str(int(charOneDict["health"]) - damage_calculator(charTwoDict, charOneDict, 25))
                        print("Player one protect, but player two's move broke through it and deals partial damage!")
                        print_player_move("two", "one", "protected heavy attack", charOneDict["health"])
                    elif moveTwo == "2":
                        charTwoDict["health"] = str(int(charTwoDict["health"]) - damage_calculator(charTwoDict, charTwoDict, 40))
                        print("Player two uses a quick attack, but player one protects and player one hurts themself!")
                        print(f"Player two is now at {charTwoDict["health"]} HP")
                    elif moveTwo == "3":
                        print("Both protected, nothing happened")

            else:
                print("Please only select 1, 2, or 3, on of the inputs was invalid")

        end_game()

    player_choice()

def main():
    while True:
        whatToDo = input("Manage characters (1), battle (2), or exit (3)? ")
        if whatToDo == "1":
            character_manager()
        elif whatToDo == "2":
            battle_main()
        elif whatToDo == "3":
            exit()
        else:
            print("Invalid input.")

main()
