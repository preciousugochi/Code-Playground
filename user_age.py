def user_age():
    year = 2023
    birth_year = int(input())

    age = year - birth_year

    if len(str(birth_year))== 4:
        
        print(f"You are {age} years old.")
    else:
        print("invalid year")

user_age()   