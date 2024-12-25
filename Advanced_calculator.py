unit = input("Enter the operation you want to Execute(+,-,*,/,^) ")

o1 = float(input("Enter the first operator = "))
o2 = float(input("Enter the second operator = "))

if unit == "+":
    print(o1+o2)

elif unit == "-":
    print(o1-o2)

elif unit == "*":
    print(o1*o2)

elif unit == "/":
    if o2 != 0:
        print(o1//o2)
    else:
        print("Error division by 0!")

elif unit =="^":
    print(o1**o2)

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
        unit = input("Enter the operation you want to Execute(+,-,*,/,^) ")

        o1 = float(input("Enter the first operator = "))
        o2 = float(input("Enter the second operator = "))

        if unit == "+":
         print(o1+o2)

        elif unit == "-":
            print(o1-o2)

        elif unit == "*":
            print(o1*o2)

        elif unit == "/":
            if o2 != 0:
                print(o1//o2)
            else:
                print("Error division by 0!")

        elif unit =="^":
            print(o1**o2)

        else:
            print("Invalid Operation Taken")

        cont=input("Continue (y/n)")