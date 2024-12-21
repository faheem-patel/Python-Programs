num=int(input("enter the number to cheak: "))
isprime=True

for i in range(2,num//2):
    if (num %i ==0):
        print("It is not Prime number")
        break
else:
    print("It is a Prime number")
   