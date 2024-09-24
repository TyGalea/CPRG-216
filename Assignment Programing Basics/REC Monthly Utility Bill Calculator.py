# REC Monthly Utility Bill Calculator - CPRG216 Assignment Programming Basics
#
# This program calculates the customer’s total monthly utility bill in CDN$.
# The customer will first enter their account number, month, type of electricity plan,
# amount of electricity used (in kWh), type of natural gas plan, amount of natural gas 
# used (in GJ), and the province. The program will then calculate and display the customer's monthly
# utility charge by adding together the fixed monthly fee, the cost of electricity,
# the cost of gas, and the fixed monthly transaction fee. The program then calculates and display 
# the province sales tax from the customers province. Lastly, the program displays the total
# amount due by adding the monthly utility charge and province sales tax
#
# Author Tyler Galea
# Version 2023-02-17

# Gets all of the customers information
print("Welcome to Responsible Energy bill calculator!\n")
accountNum = int(input("Enter the account number: "))
month = int(input("Enter the month number, i.e. for January, enter 1: "))
electricityPlanType = input("Enter the electricity plan type (EFR or EVR): ")
electricityAmount = int(input("Enter amount of electricity used in month " + str(month) + " (in kWh): "))
gasPlanType = input("Enter the gas plan type (GFR or GVR): ")
gasAmount = int(input("Enter amount of gas used in month " + str(month) + " (in GJ): "))
province = input("Enter the province abbreviation (2 letters): ")
print("Thank you!")

# Adds the fixed monthly fee to the monthly utility charge
monthlyUtilityCharge = 127.86

# Adds the cost of electricity to the monthly utility charge
if(electricityPlanType == "EFR"):
    if(electricityAmount <= 1000):
        monthlyUtilityCharge += electricityAmount * (8.86 * 0.01)
    else:
        monthlyUtilityCharge += 1000 * (8.86 * 0.01) + (electricityAmount - 1000) * (9.97 * 0.01)
elif(electricityPlanType == "EVR"):
    monthlyUtilityCharge += electricityAmount * (9.66 * 0.01)

# Adds the cost of gas to the monthly utility charge
if(gasPlanType == "GFR"):
    if(gasAmount <= 950):
        monthlyUtilityCharge += gasAmount * (4.83 * 0.01)
    else:
        monthlyUtilityCharge += 900 * (4.83 * 0.01) + (gasAmount - 950) * (6.24 * 0.01)
elif(gasPlanType == "GVR"):
    monthlyUtilityCharge += gasAmount * (4.17 * 0.01)

# Adds fixed monthly transaction fee to the monthly utility charge
monthlyUtilityCharge += 1.40

# Displays the monthly utility charge
print("Monthly Utility Charge: $", format(monthlyUtilityCharge, '.2f'), sep='')

# Calculate the province sale tax
if(province == "AB" or province == "BC" or province == "MB" or province == "NT" 
or province == "NU" or province == "QC" or province == "SK" or province == "YT"):
    provinceSaleTax = monthlyUtilityCharge * 0.05
elif(province == "ON"):
    provinceSaleTax = monthlyUtilityCharge * 0.13
elif(province == "NB" or province == "NL" or province == "NS" or province == "PE"):
    provinceSaleTax = monthlyUtilityCharge * 0.15

# Displays the province sale tax and total amount due
print("Provincial Sales Tax: $",format(provinceSaleTax, ".2f"), sep='')
print("Total Amount Due Now: $",format(monthlyUtilityCharge + provinceSaleTax, ".2f"), sep='')