num =int(input("Enter a number to generate its multiplication table: "))

if num == 0:
    print("You are MAD!!")

else:
    i =1

    while i <= 10:
        print(num," * ",i," = ",i*num)
        i +=1
