#Pedro Souza, Word Counter

from word_counter import count #imports count function

#Based off choice, either leaves, or runs the word counter
def main(choice):
    if choice == "1":
        count(input("\nWhat is the relative file path for your document? (needs to be in the project files)\nChoice: "))
    elif choice == "2":
        print("\nBye bye!")
        exit()
    else: #Else statement for invalid inputs, gives an error message and asks again
        print("\nThat was an invalid answer, please only answer with (1) or (2)")

#Repeatedly asks user what to do, gives either (1) run the word counter or (2) exit options
while True:
    main(input("\nWould you like to:\n\t1: Count words\n\t2:Exit\n\tChoice: "))