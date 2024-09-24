sum = 0
num = int(input("Enter an integer > 1: "))
for i in range(1, num + 1):
    sum += i
print("\nThe average of the integers 1..." + str(num),"is", sum / num)