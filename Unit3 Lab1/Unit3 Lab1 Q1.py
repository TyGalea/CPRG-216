import math

#  Function:  circumference
#
#  This function finds the circumference of a circle given its radius 
#
#  Parameters:  radius - required parameter (int) - the radius of the circle
#  Returns   :  circumference - (float) - the  circumference of the circle
def circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

#  Function: area
#
#  This function finds the area of a circle given its radius 
#
#  Parameters:  radius - required parameter (int) - the radius of the circle
#  Returns   : area - (float) - the area of the circle
def area(r):
    area = math.pi * r ** 2
    return area

#  Function: main
#
#  This function asks the user to give the radius of a circle
#  and then displays the circles circumference and area
#
#  Parameters:  None
#  Returns   : None
def main():
    radius = int(input("Give the radius of a circle: "))
    print("Circumference:", format(circumference(radius), ".3f"), end=', ') 
    print("Area:", format(area(radius), ".3f"))
    
if __name__ == "__main__":
    main()