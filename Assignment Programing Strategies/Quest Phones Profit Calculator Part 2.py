# Quest Phones Profit Calculator - CPRG216 Assignment Programming Strategies
#
# This program finds the total profit for quest phones for a given time period.
# The user will enter a time period and then the quantity sold for each product
# for each day in the time period. The program will then calculate the total 
# profit for the time period. Lastly, the program the tell the user if the total 
# profit achieved the daily profit goal.
# 
# Author Tyler Galea, Urooba Ejaz, Lakshita Sethi
# Version 2023-03-17

# The price of one unit in each category
CATEGORY1 = 127.68
CATEGORY2 = 105.47
CATEGORY3 = 80.23
CATEGORY4 = 69.67
CATEGORY5 = 54.57
# The days of the week
WEEK = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# The daily profit goal
DAILY_PROFIT = 10000.00

# The program runs until the user picks the exit option and then displays that the program ended successfully
exit = False
while not exit:
    # Displays the time period options
    print("Quest Phones Profit Calculator\n")
    print(f'{"Option":>8}     Time Period')
    print(f'{"1":>8}     Single Day')
    print(f'{"2":>8}     Entire Week')
    print(f'{"3":>8}     Only Weekdays: Mon-Fri')
    print(f'{"4":>8}     Only Weekend Days: Sun & Sat')
    print(f'{"0":>8}     Exit')
    # Asks user to enter their option and checks that it is a valid input
    option = input("Enter menu option: ")
    # Creates a list of the days the user has chosen
    days = []
    if not option.isdigit():
        print("Invalid menu selection... Try again\n")
    elif int(option) == 1:
        # If the user picks option 1 "Single Day", it asks the user to enter a day of the week and checks that it is a valid input
        while len(days) == 0:
            possibleDay = input("Enter a specific day [Sun, Mon, Tue, Wed, Thu, Fri, Sat]: ").capitalize()
            for day in WEEK:
                if possibleDay == day:
                    days.append(possibleDay)
                    optionPicked = day
    elif int(option) == 2:
        days = WEEK
        optionPicked = "Entire Week"
    elif int(option) == 3:
        days = WEEK[1:6]
        optionPicked = "Only Weekdays: Mon-Fri"
    elif int(option) == 4:
        days = WEEK[::6]
        optionPicked = "Only Weekend Days: Sun & Sat"
    elif int(option) == 0:
        exit = True
    else:
        print("Invalid menu selection... Try again\n")
    # Begins total profit calculations if the user has picked a valid time period
    if len(days) > 0:
        totalProfit = 0
        # Gets the profit from each day
        for day in days:
            print("For", day)
            next = False
            dayProfit = 0.00
            # The user adds the quantity sold of each product for the day until they exit
            while not next:
                # Asks user to enter a product number and checks that it is a valid input
                category = input("Enter product number (1-5 or 0 to stop): ")
                if not category.isdigit():
                    print("Product number must be between 1 and 5 or 0 to exit... Try Again")
                else:
                    if int(category) > 0 and int(category) <= 5:
                        quantityIsDigit = False
                        
                        # Asks the user to enter the quantity sold and checks that it is a valid input
                        while not quantityIsDigit:
                            quantity = input("Enter quantity sold: ")
                            if quantity.isdigit():
                                quantityIsDigit = True
                    # Adds to the days profit based on the product number and quantity sold
                    if int(category) == 1:
                        dayProfit += int(quantity) * CATEGORY1
                    elif int(category) == 2:
                        dayProfit += int(quantity) * CATEGORY2
                    elif int(category) == 3:
                        dayProfit += int(quantity) * CATEGORY3
                    elif int(category) == 4:
                        dayProfit += int(quantity) * CATEGORY4
                    elif int(category) == 5:
                        dayProfit += int(quantity) * CATEGORY5
                    elif int(category) == 0:
                        next = True
                    else:
                        print("Product number must be between 1 and 5 or 0 to exit... Try Again")
            totalProfit += dayProfit
        # Displays the total profit for the time period
        print("\nTotal Profit for the ", optionPicked, " is: $", format(totalProfit, ',.2f'), sep='')
        # Calculates and displays if the daily profit goal was met
        if totalProfit > len(days) * DAILY_PROFIT:
            print("Successfully achieved daily profit goal of $", format(DAILY_PROFIT, ',.2f'), '/day for option "', optionPicked, '"\n', sep='')
        else:
            print("Did not achieved daily profit goal of $", format(DAILY_PROFIT, ',.2f'), '/day for option "', optionPicked, '"\n', sep='')
print("Program ended successfuly")