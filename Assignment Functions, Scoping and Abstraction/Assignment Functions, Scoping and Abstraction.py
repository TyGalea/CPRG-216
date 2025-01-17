# Quest Phones Profit Calculator - CPRG216 Assignment Programming Strategies
#
# This program asks the user about the cost of paint, the number of rooms to paint and the amount of
# coats to apply to each room. It asks the user details about each room such as the dimensions and the
# amount and size of the doors and windows in each room. The program will print a summary of each room.
# Lastly, a Customer Quote will be printed including the final estimated cost.
# 
# Author Tyler Galea, Urooba Ejaz, Lakshita Sethi
# Version 2023-04-09

# area that 1 gallon of paint can paint
AREA_PER_GALLON = 175
# labor cost per area to paint
LABOR_COST_PER_AREA = 0.18
# labor cost per door and window to tape
LABOR_COST_PER_DOOR_WINDOWS = 10.00
# the profit margin
PROFIT_MARGIN = 1.30

# imports math function for ceil() to round gallons up
import math

#  Function: main
#
#  This function first gets the paint price, the number of coats, and the number of rooms.
#  Then for every room it gets the type of room, calculates the area of the room and removes
#  the area of the doors and windows of the room. The area is multiplied by the number of coats
#  and a summary of the room is printed. The total number of windows and doors and the total are
#  are updated. This loops through every room that is being painted. Lastly, the function prints out
#  a Customer Quote that has the number of coats of paint, the total area to paint, the gallons of paint
#  needed, and the final cost.
#
#  Parameters: None
#  Returns   : None
def main():
    print("The Painter's Company Estimating Tool\n")
    price = getPaintPrice()
    coats = getNumberOfCoats()
    rooms = getNumberOfRooms()
    totalArea = 0
    totalWindowDoors = 0
    for room in range(1, rooms + 1):
        option = roomsMenu(room)
        area = computeRoomArea(option)
        windowDoors = getNumberWindowsDoors()
        totalWindowDoors += windowDoors
        area -= computeWindowsDoorsArea(windowDoors)
        area *= coats
        printRoomSummary(room, area, price)
        totalArea += area
    print("\nCustomer Quote for All", rooms, "rooms:")
    print(format("        Coats of paint to be appied", "35s"), ": ", coats, sep='')
    print(format("        Total area to be painted", "35s"), ": ", format(totalArea, ".1f"), " sq ft.", sep='')
    gallons = math.ceil(computeGallons(totalArea))
    print(format("        Paint required", "35s"),": ", gallons, " gallons", sep='')
    paintRequiredArea = gallons * AREA_PER_GALLON
    totalCost = computePrintPrice(paintRequiredArea, price) 
    totalCost += totalArea * LABOR_COST_PER_AREA
    totalCost += totalWindowDoors * LABOR_COST_PER_DOOR_WINDOWS
    totalCost *= PROFIT_MARGIN
    print(format("        Total customer estimate", "35s"), ": $", format(totalCost, ".2f"), sep='')

#  Function: getPaintPrice
#
#  This function asks the user for the paint price and returns it
#
#  Parameters: None
#  Returns   : price - (float) - the paint price
def getPaintPrice():
    price = float(input("Enter price of paint: "))
    return price

#  Function: getNumberOfCoats
#
#  This function asks the user for the number of coats of paint to apply and returns it
#
#  Parameters: None
#  Returns   : coats - (int) - the number of coats of paint to apply
def getNumberOfCoats():
    coats = int(input("Enter number of coats of paint to apply (1-4): "))
    return coats

#  Function: getNumberOfRooms
#
#  This function asks the user for the number of rooms they want to paint and returns it
#
#  Parameters: None
#  Returns   : rooms - (int) - the number of to paint
def getNumberOfRooms():
    rooms = int(input("How many rooms do you want to paint?: "))
    return rooms

#  Function: roomsMenu
#
#  This function asks the user for the shape of the current room and returns it
#
#  Parameters: room - required parameter (int) - the room number
#  Returns   : option - (int) - the chosen room type
def roomsMenu(room):
    print("\nRoom:", room)
    print("Select the shape of the room:")
    print("1 - Rectangular")
    print("2 - Square")
    print("3 - Custom")
    option = int(input("Option: "))
    return option

#  Function: computeRoomArea
#
#  This function calls the appropriate function to calculate the area of the room based off
#  the shape of the room. It then returns the area of the room.
#
#  Parameters: option - (int) - the chosen room type
#  Returns   : area - (float) - the area of the room
def computeRoomArea(option):
    if option == 1:
        area = computeRectangleWallsArea()
    elif option == 2:
        area = computeSquareWallsArea()
    elif option == 3:
        area = computeCustomWallsArea()
    return area

#  Function: getNumberWindowsDoors
#
#  This function asks the user for the amount of windows and doors in the room and returns it
#
#  Parameters: None
#  Returns   : windowsDoors - (int) - the amount of windows and doors in the room
def getNumberWindowsDoors():
    windowsDoors = int(input("\nHow many windows and doors are in the room? "))
    print()
    return windowsDoors

#  Function: printRoomSummary
#
#  This function prints out a summary of the room containing the area to be painted, the paint 
#  required, and the approximate cost of the paint
#
#  Parameters: room - required parameter (int) - the room number
#              area - required parameter (float) - the area to paint for the room
#              price - required parameter (float) - the paint price
#  Returns   : None
def printRoomSummary(room, area, price):
    print("\nFor Room:", room)
    print(format("        Area to be painted", '26s'), ": ", area, " sq ft.", sep='') 
    print(format("        Paint required", '26s'), ": ", format(computeGallons(area), ".2f"), " gallons", sep='') 
    print(format("        Paint cost(approx)", '26s'), ": $", format(computePrintPrice(area, price), ".2f"), sep='')

#  Function: computeWindowsDoorsArea
#
#  This function asks the user for the length and width of ever door and window in the room. 
#  It will then calculate the total area of all the doors and windows in the room and returns it.
#
#  Parameters: windowsDoors - required parameter (int) - the amount of windows and doors in the room 
#  Returns   : area - (float) - the total area of the windows and doors in the room
def computeWindowsDoorsArea(windowsDoors):
    area = 0
    for windowDoor in range(1, windowsDoors + 1):
        length = float(input("Enter length for window/door " + str(windowDoor) + " in feet: "))
        width = float(input("Enter width  for window/door " + str(windowDoor) + " in feet: "))
        area += computeRectangleArea(length, width)
    return area

#  Function: computeRectangleWallsArea
#
#  This function asks the user for the length, width, and height of the room. 
#  It will then calculate the total area of the room and returns it.
#
#  Parameters: None
#  Returns   : area - (float) - the total area of room
def computeRectangleWallsArea():
    length = float(input("\nEnter the length of the room in feet: "))
    width = float(input("Enter the width  of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    area = 2 * computeRectangleArea(length, height) + 2 * computeRectangleArea(width, height)
    return area

#  Function: computeRectangleArea
#
#  This calculates the area of a rectangle with a length and width and returns it.
#
#  Parameters: length - required parameter (float) - the length of the rectangle
#              width - required parameter (float) - the width of the rectangle
#  Returns   : area - (float) - area of the rectangle
def computeRectangleArea(length, width):
    area = length * width
    return area

#  Function: computeSquareWallsArea
#
#  This function asks the user for the length of one wall and height of the room. 
#  It will then calculate the total area of the room and return it.
#
#  Parameters: None
#  Returns   : area - (float) - the total area of room
def computeSquareWallsArea():
    length = float(input("Enter length of one wall in feet    : "))
    height = float(input("Enter the height of the room in feet: "))
    area = 4 * computeRectangleArea(length, height)
    return area
    
#  Function: computeCustomWallsArea
#
#  This function asks the user for the number of walls in the room and the length 
#  and height of each wall. It will then calculate the total area of the room and 
#  return it.
#
#  Parameters: None
#  Returns   : area - (float) - the total area of room
def computeCustomWallsArea():
    walls = int(input("\nHow many wall are there in the room? "))
    area = 0
    for wall in range(1, walls + 1):
        length = float(input("Enter the length of wall " + str(wall) + " in feet: "))
        height = float(input("Enter the height of wall " + str(wall) + " in feet: "))
        area += computeRectangleArea(length, height)
    return area

#  Function: computeGallons
#
#  This function calculates the total gallons of paint required and returns it
#
#  Parameters: area - required parameter (float) - the total area to paint
#  Returns   : gallons - (float) - the gallons of paint required
def computeGallons(area):
    gallons = area / AREA_PER_GALLON
    return gallons

#  Function: computePrintPrice
#
#  This function calculates the total the total cost of the paint and returns it
#
#  Parameters: area - required parameter (float) - the total area to paint
#              price - required parameter (float) - the paint price
#  Returns   : cost - (float) - the total cost of the paint
def computePrintPrice(area, price):
    cost = area / AREA_PER_GALLON * price
    return cost

if __name__ == "__main__":
    main()