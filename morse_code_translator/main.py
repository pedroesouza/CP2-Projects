#Pedro Souza, Morse code translator

#lists for translating, alphabet and morse code, they are in the same order
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', " "
]

morseCode = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", 
    "..-", "...-", ".--", "-..-", "-.--", "--..", 
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", " "#as you can see, " " (space) is the last on both lists, this makes it not be translated, but moved over (so that multiple word strings have a double space to separate words)
]

#BOTH FUNCTIONS are nearly identical, so the explanantion will be on the first (I made them separate functions to improve readability and not have statements that are like 7 indents forward)

#This function translates english to morse code
def morse_code_translation():
    #Creating a variable to the translated text (morse code, currentTranslation) and the one being translated (english, currentTranslated)
    currentTranslation = []
    currentTranslated = []

    while True: #Loop runs until the word is done
        next = input("What is your next letter, number, or space? (press enter with nothing to end the word) ") #Save variable for the next letter in the word

        for i in morseCode: #Loops through every morse code combination (i)
            try: #Try finding the location of the chosen next letter on alphabet
                alphabetLocation = alphabet.index(next) #Save the location as a variable
            except: #If you can't find the location
                if list(next) == []: #When the user types jsut *enter*, the translating is done, loop ended, and final translation/original are printed
                    print(f"English: {''.join(currentTranslated)}, Morse code: {''.join(currentTranslation)}")
                    break 
                else: #If the input is a character that is not on the list and isnt *enter*, it is ignored and you get an invalid input message
                    print("Invalid input, try again!")

            morseCodeLocation = morseCode.index(i) #Save how many times the loop has gone (), aka the location of variable i in the morse code list

            if alphabetLocation == morseCodeLocation: #if i is the translation of the letter
                currentTranslation.append(i) #Add the morse code to the translation
                currentTranslated.append(next) #Put the letter in the original word
            else:
                continue #If not, try the next morse code code

#This function translates morse code to english, almost the same as the one before, changes will have comments
def english_translation():
    #Creating a variable to the translated text (english, currentTranslation) and the one being translated (morse code, currentTranslated)
    currentTranslation = []
    currentTranslated = []

    while True:
        next = input("What is your next morse code? (input in a .-. format, press space for spaces, just an empty enter to leave) ") #Save variable for the next morse code being translater
        
        for i in alphabet: #Loops through every letter and number (i)
            try: #Try finding the location of the chosen morse code code on alphabet
                morseCodeLocation = morseCode.index(next)
            except:
                if list(next) == []:
                    print(f"Morse code: {''.join(currentTranslated)}, English: {''.join(currentTranslation)}")
                    break
                else:
                    print("Invalid input, try again!")

            alphabetLocation = alphabet.index(i) #Save how many times the loop has gone (), aka the location of variable i in the alphabet list
            
            if alphabetLocation == morseCodeLocation:
                currentTranslation.append(i) #Add the letter to the translation
                currentTranslated.append(next) #Put the code in the original morse code

#Main UI function
def main():
    while True: #Loops until broken
        whatToDo = input("Would you like to translate from (1:) morse code, (2:) english to the other, or (3) leave the program? ") #Asks user what they want to translate (or leave)
        
        #Run corresponding function based on answer
        if whatToDo == "1": 
            english_translation()
        elif whatToDo == "2":
            morse_code_translation()
        elif whatToDo == "3": #Says bye if leave
            print("Bye bye!")
            break
        else: #Error handling/idiot proofing
            print("Invalid input, try again!")

main() #Starts off code