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
#FOR continuation
continue_calc = True
    #For more continuation
    
cont=input("Continue (y/n)")
    
if cont=="n":
    continue_calc = False
else:
    while continue_calc == True:
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