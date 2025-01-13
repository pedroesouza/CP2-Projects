#Pedro Souza, Financial Calculator

#Would you like to:
#1. Calulate length of saving for goal
#2. Calculate compund interest
#3. Get budget allocation help
#4. Calculatdiscount and tax slae price
#5. Calculate tip

def calc_tip():
    ogPrice = input("What was the original price?")
    taxPercent = input(f"What % of tax is in your state?")
    finalPrice = ogPrice * (taxPercent+1)
    return finalPrice

def calc_price():
    pass

def budget():
    input("How much money do you have this month?")
    print("30 percent rent 10 percent food, ten percent fun, 20 percent savings, and the leftover 30 percent should go to medical bills, debt, religious offerings, charity, or any other thing")

def calc_compound():
    pass

def calc_goal():
    deposit = input("How much is your monthly deposit?")
    goal = input("What is your goal?")

    try:
        goal = int(goal)
    except:
        goal = input("ERROR. What is your goal, please only answer with integers?")
        
    try:
        deposit = int(deposit)
    except:
        deposit = input("ERROR. How much is your monthly deposit, please only answer with integers?")

    totalTime = (goal // deposit) + 1
    return totalTime

def main():
    choice = input("\nWould you like to\n1. Calulate length of saving for goal\n2. Calculate compund interest\n3. Get budget allocation help\n4. Calculate discount and tax slae price\n5. Calculate tip\n")

    if choice == "1":
        print(f"It will take you {calc_goal()} months to complete your assignment.")

    if choice == "2":
        calc_compound()

    if choice == "3":
        budget()
    
    if choice == "4":
        calc_price()

    if choice == "5":
        calc_tip()

main()
