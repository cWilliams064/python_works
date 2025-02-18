tickets = input("How many ticket's would you like? ")
tickets = int(tickets)

if tickets <= 0:
    print("Please enter a number greater than 0.")
else:
    total_price = 0

    for ticket in range(1, tickets + 1):
        age = input(f"Enter the age for ticket #{ticket}: ")
        age = int(age)

        if age < 3:
            price = 0
        elif (age >= 3) and (age <= 12):
            price = 10
        elif age > 12:
            price = 15
    
        total_price += price

    print(f"Your total price is {total_price} dollars.")
