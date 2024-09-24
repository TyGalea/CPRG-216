calculatorOpen = True
while calculatorOpen:
    print("Simple Calculator\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Exit\n")
    menu = int(input("Enter menu option: "))
    if(menu == 0):
        print("Calculator app closed")
        calculatorOpen = False
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if(menu == 1):
            print(num1, "+", num2, "=", num1 + num2)
        elif(menu == 2):
            print(num1, "-", num2, "=", num1 - num2)
        elif(menu == 3):
            print(num1, "*", num2, "=", num1 * num2)
        elif(menu == 4):
            if(num2 == 0):
                print("Cannot divide by 0")
            else:
                print(num1, "/", num2, "=", num1 / num2)
        print()
