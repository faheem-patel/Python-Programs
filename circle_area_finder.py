radius=float(input('Enter the radius of a circle: '))
pi=(22/7)

cont=True

area=pi*(radius**2)

print('Area is ',area)
advanced=input('continue(y/n) ')

if advanced == 'y':
    cont=True

else:
    cont=False

while cont == True:

    radius=float(input('Enter the radius of a circle: '))
    area=pi*(radius**2)

    print('Area is ',area)
    advanced=input('continue(y/n) ')