
while True:
    
    print("Choose an area formular to use: area1 or area2? ")
    
    area=input("area1 or area2:  ")
    if area in ('area1') or area in ('Area1'):
        print("For area1")
        x= float(input(" Enter side 1:  "))
        y=float(input(" Enter side 2:  "))
        z=float(input("Enter side 3:  "))

# s is the semi-perimeter to be used in the this formula

        s = (x + y + z)/2
        area1 = (s*(s-x)*(s-y)*(s-z)) ** 0.5
        print(f"The area is calculated as follows:  (s*(s-x)*(s-y)*(s-z)) ** 0.5,\n So the answer is:  {area1}")
        
    elif area in ('area2') or area in ('Area2'):
        print("For area2")
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area2 = (base*height)*0.5
        print(f"The area is calculated as follows: (base*height)*0.5, \n  So the answer is:  {area2}")

    else:
        print("Invalid input") 
        
    loop=input("Do you want to do another calculaton? Yes or No:  ")
    if loop in ('yes') or loop in ('Yes'):
        continue
    else:
            break
   
        
        






