#Import random to get a random item in a list, import string to more easily make lowercase, uppercase, or digits (in string form) list
import random
import string

#using string and also just manual imputs to make lists of lower and uppercase, numbers, and special characters for password generation 
lowercaseLetters = list(string.ascii_lowercase)
uppercaseLetters = list(string.ascii_uppercase)
numbersList = list(string.digits)
specialCharacters = list("\"'!@#$%^&*()+-_=+,<.>;:[\\]{}")

#The function that handles the making of the password based on the data from the other two functions
def make_password(amount, uppercase, num, special_char): #Paramaters are the amount of characters, and wehther the password has uppercase, numbers, special characters (y or n answer)
    
    rngList = [1]  #Default the random character list to only lowercase
    

    #If statements to decide whether the random character list will have different options based on user choice
    if uppercase.lower() == "y":
        rngList.append(2)
    if num.lower() == "y":
        rngList.append(3)
    if special_char.lower() == "y":
        rngList.append(4)
    
    #While true loop start (goes until function stops)
    while True:

        #Reset password and checkers for password valitidy
        funcPassword = ""
        hasUp = False
        hasNum = False
        hasSpecChar = False

        for i in range(amount): #Repeat for the length of the password
            #randomlly selects one of up to 4 categories (upper, lower, number, special characters), the categories can go down to one based on user choice, adds to password
            rng = random.choice(rngList)
            if rng == 1:
                funcPassword += random.choice(lowercaseLetters)
            elif rng == 2:
                funcPassword += random.choice(uppercaseLetters)
                hasUp = True
            elif rng == 3:
                funcPassword += random.choice(numbersList)
                hasNum = True
            elif rng == 4:
                funcPassword += random.choice(specialCharacters)
                hasSpecChar = True
        
        #Makes sure the password is valid (has all needed things), if it isnt, restart the process (go back to while true loop start)
        if (uppercase.lower() != "y" or hasUp) and (num.lower() != "y" or hasNum) and (special_char.lower() != "y" or hasSpecChar):
            return funcPassword  #if valid, return

#Ask function, this is a function to improve code readability and facilitate idiot proofing (which is the bulk of the function)
def ask(functionLength, functionIncludeUpper, functionIncludeNumbers, functionIncludesSpecial): #4 Parameters that were asked for in main function, those will all be used in the make_password function to determine different things

    #This whole chunk is just making sure the parameters fit the needed format and reasking questions as needed
    try:
        functionLength = int(functionLength)
    except:
        return ask(input("ERROR, How many characters?, the minimum is 3 and you can only answer with integers. "), functionIncludeUpper, functionIncludeNumbers, functionIncludesSpecial)
    
    if functionLength <= 3:
        return ask(input("ERROR, How many characters?, the minimum is 3 and you can only answer with integers. "), functionIncludeUpper, functionIncludeNumbers, functionIncludesSpecial)

    if functionIncludeUpper not in ["n", "y"]:
        return ask(functionLength, input("ERROR, Would you like to include uppercase letters? (y/n) "), functionIncludeNumbers, functionIncludesSpecial)

    if functionIncludeNumbers not in ["n", "y"]:
        return ask(functionLength, functionIncludeUpper, input("ERROR, Would you like numbers? (y/n) "), functionIncludesSpecial)

    if functionIncludesSpecial not in ["n", "y"]:
        return ask(functionLength, functionIncludeUpper, functionIncludeNumbers, input("ERROR, Would you like special characters? (y/n) "))

    return functionLength, functionIncludeUpper, functionIncludeNumbers, functionIncludesSpecial  #Returns idiot proofed values back to function call in main

#This is the main (mostly UI) function
def main():
    while True:
        length, includeUpper, includeNumbers, includeSpecial = ask(input("How many characters? "), input("Would you like to include uppercase letters? (y/n) "), input("Would you like numbers? (y/n) "), input("Would you like special characters? (y/n) "))
        
        passwords = [make_password(length, includeUpper, includeNumbers, includeSpecial) for i in range(4)]#creates a list of passwords (4 total) by calling the make password fucntion in a loop inside the list
        for i, password in enumerate(passwords, 1):#
            print(f"Generated password {i}: {password}")
        
        repeat = input("Would you like to generate more passwords? (y/n) ")#Ask user if they want to leave
        if repeat.lower() != "y":#If the answer is not yes, end the repeating loop
            break

main() #Call main function to start the whole program
