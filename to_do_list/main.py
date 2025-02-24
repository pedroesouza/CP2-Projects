#The check function rewrites every line, but when it is the selected line, it goes though a process of splitting the line, and replacing the second half with it's oposite
def check(lineChecked):
    #Sets current line variable to 0, this will go up by one every line
    currentLine = 0

    #Idiot proofing
    try: 
        lineChecked = int(lineChecked) 
    except:
        print("Please only answer with integers")
        return

    #"Looks" for the selected line, splits it in two, and changes the second half to it's oposite
    with open("to_do_list/list.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            currentLine += 1
            if currentLine != lineChecked:
                file.write(line)
            else:
                lineString = line.split(": ")
                if lineString[1].strip() == "False":
                    file.write(f"{lineString[0]}: True\n")
                else:
                    file.write(f"{lineString[0]}: False\n") 
        file.truncate()

#Add function simply appends a new line as written by the user, defaults to false
def add(added):
    with open("to_do_list/list.txt", "a") as file:
        file.write(f"{added}: False\n")

#The remove function rewrties every line but the one that was selected to be deleted
def remove(lineDeleted):
    currentLine = 0

    #Idiot proofing
    try: 
        lineDeleted = int(lineDeleted)
    except:
        print("Please only answer with integers")
        return
    
    #The whole, delete line, rewrite if not the chosen line deal
    with open("to_do_list/list.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            currentLine += 1
            if currentLine != lineDeleted:
                file.write(line)
        file.truncate()


#Main UI function that calls other functions
def main():
    #Prints the current to do list
    with open("to_do_list/list.txt", "r") as file:
        fileContents = file.read()
        print(fileContents)

    #Asks user what they want to do
    choice = input("Would you like to add (type 1), remove (2), check an item off (3), or leave (4) ")
   
    #Does/calls the function that does each selected activity
    if choice == "1":
        add(input("What would you like to add? "))
    elif choice == "2":
        remove(input("What row would you like to delete? (counting starts at 1 on the first task) "))
    elif choice == "3":
        check(input("What row would you like to check off? (counting starts at 1 on the first task) "))
    elif choice == "4":
        exit() #terminates the code

#Runs main function until the code is terminatied
while True:
    main()