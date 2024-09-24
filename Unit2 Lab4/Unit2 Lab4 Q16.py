territories = ("Northwest Territories", "Yukon", "Nunavut")
terrPopuList = {}
terrPopuList[territories[0]] = int(input("Enter Population for Northwest Territories: "))
terrPopuList[territories[1]] = int(input("Enter Population for Yukon: "))
terrPopuList[territories[2]] = int(input("Enter Population for Nunavut: "))
print(f'{"Territory":22s} {"Population":>22s}')
print("=============================================")
for territory, population in terrPopuList.items():
    print(f'{territory:22s} {population:>22,}')
print("=============================================")
print(f'{"Total":22s} {terrPopuList.get("Northwest Territories") + terrPopuList.get("Yukon") + terrPopuList.get("Nunavut"):>22,}')