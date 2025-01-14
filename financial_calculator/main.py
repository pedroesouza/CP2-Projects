#Pedro Souza, Financial Calculator

#importing math for ceil function (explained in goal function))#
import math
##

#this function calculates a price based of the original price and percentage of the tip#
def calc_tip(ogPrice, tipPercent):

    #idiot proof try and except statements for invalid inputs#
    try:
        ogPrice = float(ogPrice)
    except:
        calc_tip(input("ERROR. What was the original price, please only answer with numbers?"), tipPercent)
        return

    try:
        tipPercent = float(tipPercent)
    except:
        calc_tip(ogPrice, input(f"ERROR. What % of tip would you like to give, please only answer with numbers?"))
        return
    ##

    #calculating and printing results for the functions#
    finalPrice = ogPrice * (tipPercent/100 + 1)
    print(f"The tip for your order should be ${finalPrice}")
    return
    ##

##

#this function calculates a final price by taking account taxes and discounts#
def calc_price(ogPrice, taxPercent, discount):

    #idiot proof try and except statements for invalid inputs#
    try:
        ogPrice = float(ogPrice)
    except:
        calc_price(input("ERROR. What was the original price, please only answer with numbers?"), taxPercent, discount)
        return

    try:
        taxPercent = float(taxPercent)
    except:
        calc_price(ogPrice, input(f"ERROR. What % of tax do you have to pay (google it if you dont know), please only answer with numbers?"), discount)
        return
    
    try:
        discount = float(discount)
    except:
        calc_price(ogPrice, taxPercent, input(f"ERROR. What % of your item is discounted, please only answer with numbers?"))
        return
    ##

    #calculating and printing results for the functions#
    finalPrice = ogPrice * (1 - taxPercent/100) * (1 - discount/100)
    print(f"The final price for you order should be ${finalPrice}")
    return
    ##

##

#Calculates monthly budget based on how much you made in a month and expert opinions#
def budget(money):

    #idiot proof try and except statements for invalid inputs#
    try:
        money = float(money)
    except:
        budget(input("ERROR. How much money did you make this month, please only answer with numbers?"))
        return
    ##

    #print results, simple calculations of percentages in the print statement#
    print(f"Experts recommend that you spend ${money*0.3} (30%) on rent, ${money*0.1} (10%) on food, ${money*0.2} (20%) on savings, {money*0.1} (10%) on wants, and {money*0.3} (30%) on clothing, medical, religious, charity or other expenses")
    return
    ##

##

#calculates compount inerest based on original money put in and percentage per month over a set amount of time#
def calc_compound(ogMoney, percentage, time):

    #idiot proof try and except statements for invalid inputs#
    try:
        ogMoney = float(ogMoney)
    except:
        calc_compound(input("ERROR. How much money did you originally put into the compound, please only answer with numbers?"), percentage, time)
        return
    
    try:
        percentage = float(percentage)
    except:
        calc_compound(ogMoney, input("ERROR. What is the monthly increase of the compound (percentage), please only answer with numbers?"), time)
        return

    try:
        time = float(time)
    except:
        calc_compound(ogMoney, percentage, input("ERROR. How far away in the future in years do you want to calculate, please only answer with numbers?"))
        return
    ##

    #calculate and print results#
    finalCompound = (ogMoney * (1+ (percentage/100)/12))**time
        #NOTe: the compound inerest formula over there was taken from and is explained well in https://www.thecalculatorsite.com/finance/calculators/compound-interest-formula
    print(finalCompound)
    return
    ##

##

#calculates how long it will take to reack a goal based on a monthly deposit#
def calc_goal(deposit, goal):

    #idiot proof try and except statements for invalid inputs#
    try:
        deposit = float(deposit)
    except:
        calc_goal(input("ERROR. How much is your monthly deposit, please only answer with integers?"), goal)
        return

    try:
        goal = float(goal)
    except:
        calc_goal(deposit, input("ERROR. What is your goal, please only answer with integers?"))
        return
    ##

    #calculate and prints results#
    totalTime = math.ceil(goal / deposit)
        #NOTe: math.ceil used to always round number up if decimal, which is how a real life goal would work
    print(f"It will take you {totalTime} months to complete your assignment.")
    return
    ##

##

#main UI function#
def main(choice):
    
    #runs function selected and asks their variables#
    if choice == "1":
        calc_goal(input("How much is your monthly deposit?"), input("What is your goal?"))

    elif choice == "2":
        calc_compound(input("How much money did you originally put into the compound?"), input("What is the monthly increase of the compound (percentage)?"), input("How far away in the future in years do you want to calculate?"))

    elif choice == "3":
        budget(input("How much money did you make this month?"))
    
    elif choice == "4":
        calc_price(input("What was the original price?"), input(f"What % of tax do you have to pay (google it if you dont know)?"), input(f"What % of your item is discounted?"))

    elif choice == "5":
        calc_tip(input("What was the original price?"), input(f"What % of tip would you like to give?"))
    ##

    #says bye and exit programs if user chooses so#
    elif choice == "6":
        print("\nGOODBYE!\n")
        exit()
    ##

    #idiot proof try and except statements for invalid inputs#
    else:
        main(input("ERROR\n\nWould you like to\n1. Calulate length of saving for goal\n2. Calculate compund interest\n3. Get budget allocation help\n4. Calculate discount and tax sale price\n5. Calculate tip\n6. Exit program\nPlease only answer with integers 1-5\n"))
    ##

##
#start and loop code by running and asking UI function#
while True:
    main(input("\nWould you like to\n1. Calulate length of saving for goal\n2. Calculate compund interest\n3. Get budget allocation help\n4. Calculate discount and tax sale price\n5. Calculate tip\n6. Exit program\n"))
##
