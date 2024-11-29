o1 = int(input("Enter the first operator = "))
unit = input("Enter the first letter of the operator in small alphabet = ")
o2 = int(input("Enter the second operator = "))

if unit == a:
    print(o1+o2)

elif unit == s:
    print(o1-o2)

elif unit == m:
    print(o1*o2)

elif unit == d:
    print(o1//o2)