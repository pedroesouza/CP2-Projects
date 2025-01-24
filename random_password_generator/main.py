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

def make_password(amount):
    func_password = ""
    for i in range(1, int(amount) + 1):
        rng = random.choice([1, 2, 3, 4])
        if rng == 1:
            func_password += random.choice(lowercase_letters)
        if rng == 2:
            func_password += random.choice(uppercase_letters)
        if rng == 3:
            func_password += random.choice(numbers)
        if rng == 4:
            func_password += random.choice(special_characters)

    return func_password

def main():
    main_password = make_password(input("How many characters? "))
    return main_password

password = main()
print(password)