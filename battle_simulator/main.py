import csv
import random

def character_manager():
    filePath = input("What is the relative file path to your characters? ")
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
            for i in reader:
                if i['name'].upper() == name:
                    print(i)

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
        return max(1, base_damage + (attack - defense) // 2)

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

    def player_choice():
        while int(charOneDict.get("health", 0)) > 0 and int(charTwoDict.get("health", 0)) > 0:
            print("Player 1 turn")
            moveOne = input("Would you like to heavy attack (1), quick attack (2), or defend (3)? ")
            print("Player 2 turn")
            moveTwo = input("Would you like to heavy attack (1), quick attack (2), or defend (3)? ")

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


        print("Battle over!")
        if int(charOneDict["health"]) <= 0:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

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
