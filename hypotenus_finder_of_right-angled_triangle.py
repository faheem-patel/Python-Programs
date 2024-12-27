import math


try:
    side1=float(input('Enter the length of a triangle: '))
    side2=float(input('Enter the bredth of a triangle: '))

except ValueError:
    raise ValueError('Number entered is blank!!!') from None


unit=input('enter the unit of measure: ')

hypotenus_sq=(side1**2)+(side2**2)
hypotenus=math.sqrt(hypotenus_sq)

print('hypotenus is ',hypotenus,unit)
