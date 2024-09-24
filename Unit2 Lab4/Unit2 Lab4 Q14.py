name = (input("Enter name: "))
name = name.title()
index1 = name.find(' ') + 1
index2 = name.find(' ', index1) + 1
print((name[0]) + "." + (name[index1]) + "." + (name[index2]) + ".")