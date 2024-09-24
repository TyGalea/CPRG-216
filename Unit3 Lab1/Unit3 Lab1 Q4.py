#  Function: menu
#
#  This function asks the user to pick the type of operation the user wants to perform
#  to two numbers or if they want to exit
#
#  Parameters: None
#  Returns   : menu - (int) - the menu option the user picked
def menu():
    print("Simple Calculator\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Exit")
    valid = False
    while not valid:
        menu = input("Enter menu option: ")
        if menu.isdigit():
            if int(menu) >= 0 and int(menu) <=5:
                valid = True
    return int(menu)

#  Function: add
#
#  This function adds two numbers together and returns the sum
#
#  Parameters: num1 - required parameter (float) - the first number
#              num2 - required parameter (float) - the second number
#  Returns   : sum - (float) - the sum from adding num1 and num2
def add(num1, num2):
    sum = num1 + num2 
    return sum

#  Function: subtract
#
#  This function subtracts one number from another and returns the difference
#
#  Parameters: num1 - required parameter (float) - the first number
#              num2 - required parameter (float) - the second number
#  Returns   : difference - (float) - the difference from subtracting num2 from num1
def subtract(num1, num2):
    difference = num1 - num2
    return difference

#  Function: mutilply
#
#  This function multiplies two numbers together and returns the product
#
#  Parameters: num1 - required parameter (float) - the first number
#              num2 - required parameter (float) - the second number
#  Returns   : product - (float) - the product from multiplying num1 and num2
def mutilply(num1, num2):
    product = num1 * num2
    return product

#  Function: subtract
#
#  This function divides one number from another and returns the quotient
#
#  Parameters: num1 - required parameter (float) - the first number
#              num2 - required parameter (float) - the second number
#  Returns   : quotient - (float) - the quotient from dividing num2 from num1
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by 0"
    else:
        quotient = num1 / num2
        return quotient

#  Function: main
#
#  This function asks the user for two numbers and them performs one of four 
#  operations to the two numbers and displays the results. The function continues 
#  this until the menu option is exit.
#
#  Parameters:  None
#  Returns   : None
def main():
    calculatorOpen = True
    while calculatorOpen:
        menuOption = menu()
        if(menuOption == 0):
            print("Calculator app closed")
            calculatorOpen = False
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if(menuOption == 1):
                print(num1, "+", num2, "=", add(num1, num2))
            elif(menuOption == 2):
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif(menuOption == 3):
                print(num1, "*", num2, "=", mutilply(num1, num2))
            elif(menuOption == 4):
                print(num1, "/", num2, "=", divide(num1, num2))
    
if __name__ == "__main__":
    main()