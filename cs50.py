import csv
import sql
import sqlite3
from sqlite3 import Error
from cs50 import SQL

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    UnitedStates, GreatBritain, France = 0, 0, 0
    for row in reader:
        favorite = row["Country"]
        if favorite == "UnitedStates":
            UnitedStates+=1
        elif favorite == "GreatBritain":
            GreatBritain+=1
        
        elif favorite == "France":
            France +=1
        
       


print(f"United States: {UnitedStates}")

print(f"Great Britain: {GreatBritain}")

print(f"France: {France}")


# a better more dynamic way of running the code above.
# with this, you dont have to name each country as a single variable

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["Gender"]
        if favorite in counts:
            counts[favorite]+=1
        else:
            counts[favorite]=1

for favorite in sorted(counts, key= lambda Gender: counts[Gender], reverse= True): #sorted(counts, reverse = True)
    print(f" {favorite} : {counts[favorite]}")

# to input your data and see the number of people with same data 

favorite = input("What is your gender: ")
if favorite in counts:
    print (f" we have {counts[favorite]} {favorite}s")
       
