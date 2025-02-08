from datetime import datetime
import random


f_name = input('Enter your First Name: ')
m_name = input('Enter your Middle Name: ')
l_name = input('Enter your Last Name: ')
gender=input('Enter your Gender (male/female) ')
f_name_length= len(f_name) 
full_name = f_name + " "+m_name + " "+l_name
bdate= int(input("Enter your birth year "))

def agefind ():
    date= datetime.now().year
    age=date - bdate
    
    return age
age = agefind ()


print('Generating your User ID')


x = 0
while x < f_name_length:
    print('loading.....')
    x += 1

before_name=''

if age <= 18:
    if gender == 'male':
        before_name = 'Master'

    else:
        before_name = 'Miss'

elif age > 18:

    if gender == 'male':
        before_name = 'Mr. '

    else:
        before_name = 'Mrs '

id = random.randint(10000000, 999999999999)

greet= print (f"HELLO {before_name} {f_name}, ")
info= print('This is your information and User ID :')

print(f"HELLO {before_name} {f_name},")
print('This is your information and User ID:')
print(f"Full Name: {full_name}")
print(f"User Id: {id}")