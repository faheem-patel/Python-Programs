unit = input("Enter the operation you want to Execute(a\s\m\d) ")

o1 = float(input("Enter the first operator = "))
o2 = float(input("Enter the second operator = "))

if unit == "a":
    print(o1+o2)

elif unit == "s":
    print(o1-o2)

elif unit == "m":
    print(o1*o2)

elif unit == "d":
    print(o1//o2)

else:
    print("Invalid Operation Taken")