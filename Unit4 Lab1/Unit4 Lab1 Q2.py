PI = 3.1415926

class Circle:
    numOfCircles = 0

    def __init__(self, r):
        self.radius = r
        Circle.numOfCircles += 1
    
    def area(self):
        return PI * self.radius ** 2
    
    def perimeter(self):
        return 2 * PI * self.radius
    
    def get_number_of_circles():
        return Circle.numOfCircles
    
circle1 = Circle(8)
print("Circle 1")
print("        Area      =", format(Circle.area(circle1), ".4f"))
print("        Perimiter =", format(Circle.perimeter(circle1), ".4f"))
circle2 = Circle(5)
print("Circle 1")
print("        Area      =", format(Circle.area(circle2), ".4f"))
print("        Perimiter =", format(Circle.perimeter(circle2), ".4f"))
print("Number of circles = ", Circle.get_number_of_circles())