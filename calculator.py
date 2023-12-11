

def  addition(*args):
    return sum(args)

def subtract(a,b):
    
    return a-b
    

def divide(a,b):
    
    return a/b

def multiply(*args):
    
    for i in range(0, len(args)):
        # result*=args[i]
        print(args[i])
    # return result




while True:
    
    print(' ')
    print(' ')

    print("1. Add ")
    print("2. subtract ")
    print("3. Divide ")
    print("4. Multiply ")
    print("5. Exit calculator")

    selection = input("Choose a number: (1, 2 , 3 , 4): ")

    

    if selection == '1':
        args=[]
        n = int(input("How many numbers will be used for this calculation: "))
        for i in range(n):
            arg = float(input("Enter number: "))
            args.append(arg)

        print("Your answer is: ", sum(args))

    elif selection == '2':
        a= float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Your answer is: ", subtract(a,b))

    elif selection == '3':
        a= float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Your answer is: ", divide(a,b))

    elif selection == '4':
        args =[]
        n = int(input("How many numbers will be used for this calculation: "))
        for i in range(n):
            arg = float(input("Enter number: "))
            args.append(arg)
        # return args
        multiplied = 1
        for i in range(0, len(args)):
            multiplied *= args[i]
        # return multiplied
        
            
        print("Your answer is: ", multiplied)

    elif selection == '5':
        break
        
    else:
        print("Invalid selection try again")
   
        
        
        


