amount = int(input("How much did you borrow? :  "))
repay = amount *(2/100) + amount
late_pay = amount * (5/100) + amount

query = input("Is this a late payment? yes or no ")

if query in 'yes' or query in 'Yes':
    print(f"You are to pay {late_pay} naira only.")
elif query in 'no' or query in 'No':
    print(f"Great! You are to pay {repay} naira only")
            
else:
    print("Please answer the query")
        
