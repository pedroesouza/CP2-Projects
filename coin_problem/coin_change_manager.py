import csv

# Main function to handle the coin change process
def coin_change_main():
    with open('coin_problem/currencies.csv', newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)  # Read all rows into a list

        try:
            # Ask user for the currency line (1 = USD, 2 = BRL, etc.)
            currencyLine = int(input("USD(1), BRL(2), JPY(3), or GBP(4)? "))  
            if currencyLine not in [1, 2, 3, 4]:
                print("Invalid choice")  # Invalid input
                return
            
            # Ask for the amount of money and handle possible comma issue (e.g., 100,50 -> 100.50)
            amount = float(input("How much money? ").replace(",", "."))  

            # Check if the currency has decimals, and handle them accordingly
            if currencyLine in [1, 2, 4]:  # For USD, BRL, and GBP
                # Check if there are more than 2 decimals, round and warn user
                if len(str(amount).split(".")[1]) > 2:
                    print("Money only goes to two decimals (extra decimals will be rounded).")
                amount = round(amount, 2)  # Round to 2 decimal places
            elif currencyLine == 3:  # For Yen
                # Yen doesn't support decimals, so remove the decimal portion if present
                if amount % 1 != 0:
                    print("Yen doesn't have decimals. The decimal portion will be removed.")
                amount = int(amount)  # Remove decimals for Yen
            
            amount = round(amount * 100)  # Convert amount to cents (e.g., 1.50 -> 150 cents)
            
            # If the amount is 0, print a message and return
            if amount == 0:
                print("You need 0 coins/bills.")
                return
            
            # If the amount is negative, it's an invalid input
            elif amount < 0:
                print("You are in debt, you don't get any denominations.")
                return

            # If the input is a complex number, it's not valid
            elif isinstance(amount, complex) and amount.imag != 0:
                print("You only have money in your imagination, get a job please!!")
                return
            
        except ValueError:
            # Handle invalid number input
            print("Please enter numbers.")
            return

        # Function to process the denominations and skip invalid entries in the CSV
        def process_currency_row(currencyLine, rows):
            row = rows[currencyLine]  # Get the row for the selected currency
            denominations = []  # List to store valid denominations

            # Loop through the row, skipping the name and last column (conversion rate)
            for i in range(1, len(row) - 1, 2):
                name = row[i]  # Denomination name (e.g., "$100 note")
                try:
                    # Try to convert the value to a float
                    value = float(row[i + 1])  
                    value = round(value * 100)  # Convert value to cents
                    denominations.append((value, name))  # Add to denominations list
                except ValueError:
                    # If the conversion fails (e.g., "000 note"), skip the entry
                    print(f"Skipping invalid entry: {row[i + 1]}")
                    continue

            return denominations

        # Get the list of valid denominations for the selected currency
        denominations = process_currency_row(currencyLine, rows)

        # Sort denominations from highest to lowest
        denominations.sort(reverse=True)

        # Calculate the change needed
        change = {}
        for value, name in denominations:
            if amount >= value:
                count = amount // value  # Number of coins/bills for this denomination
                amount %= value  # Remaining amount after taking out the coins/bills
                change[name] = count  # Store the count for each denomination

        # Print the change breakdown
        print("\nChange breakdown:")
        for name, count in change.items():
            print(f"{count} × {name}")

        # If there's any leftover amount, print it
        if amount > 0:
            print(f"Leftover: {amount / 100:.2f}")  # Convert cents back to currency format

