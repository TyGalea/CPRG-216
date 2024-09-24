tempList = []
exit = False
total = 0
while not exit:
    temp = float(input("Enter Temperature: "))
    if temp == 999:
        exit = True
    else:
        tempList.append(temp)
        total += temp
average = total / len(tempList)
above = 0
for temp in tempList:
    if temp > average:
        above += 1
print(above, "temperatures were above the average temperature of", format(average, ".1f"))