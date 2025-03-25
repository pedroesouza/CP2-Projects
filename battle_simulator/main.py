#Pedro Souza, Battle simulator

#Main file with all the function calls and imported libraries

#Import from the other two python files
from character import character_manager
from battle import battle_main

#Main UI function with the first question that decides what they will do, also has en exit option
def main():
    while True:
        whatToDo = input("Manage characters (1), battle (2), or exit (3)? ")
        if whatToDo == "1":
            character_manager()
        elif whatToDo == "2":
            battle_main()
        elif whatToDo == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input.")

#Calls main so the loop can start
main()

