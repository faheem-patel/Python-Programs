num =int(input('which number table you want to generate? '))

if num <10:
    x=1
    while x <= 10:
        print(num," * ",x," = ",x*num)
        x +=1

elif num == 0:
    print("You are MAD!!")