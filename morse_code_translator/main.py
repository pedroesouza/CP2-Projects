#Pedro Souza, Morse code translator
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
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", " "
]

def morse_code_translation():
    currentTranslation = []
    currentTranslated = []
    while True:
        next = input("What is your next letter, number, or space? (press enter with nothing to end the word) ")

        for i in morseCode:
            try:
                alphabetLocation = alphabet.index(next)
            except:
                if list(next) == []:
                    print(f"English: {''.join(currentTranslated)}, Morse code: {''.join(currentTranslation)}")
                    break
                else:
                    print("Invalid input, try again!")

            morseCodeLocation = morseCode.index(i)

            if alphabetLocation == morseCodeLocation:
                currentTranslation.append(i)
                currentTranslated.append(next)
            else:
                continue

def english_translation():
    currentTranslation = []
    currentTranslated = []
    while True:
        next = input("What is your next morse code? (input in a .-. format, press space for spaces, just an empty enter to leave) ")
        
        for i in alphabet:
            try:
                morseCodeLocation = morseCode.index(next)
            except:
                if list(next) == []:
                    print(f"Morse code: {''.join(currentTranslated)}, English: {''.join(currentTranslation)}")
                    break
                else:
                    print("Invalid input, try again!")

            alphabetLocation = alphabet.index(i)
            
            if alphabetLocation == morseCodeLocation:
                currentTranslation.append(i)
                currentTranslated.append(next)


def main():
    while True:
        whatToDo = input("Would you like to translate from (1:) morse code, (2:) english to the other, or (3) leave the program? ")
        if whatToDo == "1":
            english_translation()
        elif whatToDo == "2":
            morse_code_translation()
        elif whatToDo == "3":
            print("Bye bye!")
            break
        else:
            print("Invalid input, try again!")

main()