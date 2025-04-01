#Pedro Elias Souza, Coin change problem

#Main file/function just has the starting UI and choice management

#Imports the file and function with the most logic
from coin_change_manager import coin_change_main as coin_change

def main():
    start = input("Would you like to convert currency(1) or exit(2): ")
    if start == "1":
        coin_change()
    elif start == "2":
        exit()
    else:
        print("Invalid input!")

while True:
    main()