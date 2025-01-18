from datetime import datetime

def agefind ():
    date= datetime.now().year
    age=date - bdate
    
    return age


bdate= int(input("Enter your birth year "))
age = agefind ()

print(f'Your age is {age}')
