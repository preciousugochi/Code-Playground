# number 2 of the assignment

age= int(input())

if age <= 10 or age <0:
    print("Nah! You're so young ; you can't pay back")

elif age <=15 and age > 10:
    print("Oh! great, you can try again next time")

elif  age >= 16 or age == 100:
    print("Yeah! You're eligible. Come with your credentials rightaway.")

else:
    print("INVALID NUMBER!")

