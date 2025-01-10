#Pedro Souza, Financial Calculator

#Would you like to:
#1. Calulate length of saving for goal
#2. Calculate compund interest
#3. Get budget allocation help
#4. Calculatdiscount and tax slae price
#5. Calculate tip
e 
def calc_tip():
    pass

def calc_price():
    pass

def budget():
    input("What up gang, how much money are you willing to spend rn gang fan dude guy man dude man guy dude man dude ma guy fan gand bro fam bestie buddy bucko pal gang fam dude fan gant Im literally bald")

def calc_compound():
    pass

def calc_goal():
    deposit = input("How much is your monthly deposit?")
    goal = input("What is your goal?")

def main():
    choice = input("\nWould you like to\n1. Calulate length of saving for goal\n2. Calculate compund interest\n3. Get budget allocation help\n4. Calculate discount and tax slae price\n5. Calculate tip\n")

    if choice == "1":
        calc_goal()

    if choice == "2":
        calc_compound()

    if choice == "3":
        budget()
    
    if choice == "4":
        calc_price()

    if choice == "5":
        calc_tip()

main()