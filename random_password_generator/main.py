#Pedro Souza, Random Passoword Generator

import random
import string

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = [
    "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", 
    ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", 
    "}", "~", "€", "£", "©", "®", "™", "§", "¶", "°", "¢", "¤", "¥", "∞", "≠", "≈",
    "÷", "×", "√", "∑", "π", "μ", "Ω"
]

password = ""

def make_password(amount, uppercase, num, specialChar):
    funcPassword = ""
    
    hasUp = False
    hasNum = False
    hasSpecChar = False

    fails = 0

    if uppercase == "y":
        rngList += 2

    if num == "y":
        rungList += 3

    if specialChar == "y":
        rngList += 4

    for x in range (4+fails):
        for y in range(1, int(amount) + 1):
            rng = random.choice(rngList)
            if rng == 1:
                funcPassword += random.choice(lowercase_letters)
            if rng == 2:
                funcPassword += random.choice(uppercase_letters)
            if rng == 3:
                funcPassword += random.choice(numbers)
            if rng == 4:
                funcPassword += random.choice(special_characters)
            
            for z in range (1, funcPassword):

                if z in uppercase:
                    hasUp = True

def main():
    make_password(input("How many characters? "), input("Would you like to include uppercase letters?"), input("Would you like numbers?"), input("Would you like special characters?"))

password = main()
