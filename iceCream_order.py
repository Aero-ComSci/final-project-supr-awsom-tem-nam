order = []
order_cost=0.00
icecreamselection=""
icecreamsordered=0

icecreamamount=input("How many ice creams would you like to order? ")
while not icecreamamount.isdigit() or int(icecreamamount) < 1:
    print("Enter a valid number for ice cream count")
    icecreamamount=input("How many ice creams would you like to order? ")

while icecreamsordered < int(icecreamamount):
    print("Ice Cream Menu \n Chocolate: $4.50 \n Strawberry: $5.25 \n Butter Pecan: $5.50 \n Vanilla: $5.75 \n Cookie Dough: $6.25 ")

    icecreamselection=input("What ice cream would you like? ").lower()

    if icecreamselection=="chocolate":
        print("Adding chocolate ice cream to order")
        order_cost+= 4.50
        icecreamsordered+= 1
    elif icecreamselection=="strawberry":
        print("Adding strawberry ice cream to order")
        order_cost+= 5.25
        icecreamsordered+= 1
    elif icecreamselection=="butter pecan":
        print("Adding butter peacan ice cream to order")
        order_cost+= 5.50
        icecreamsordered+= 1
    elif icecreamselection=="vanilla":
        print("Adding vanilla ice cream to order")
        order_cost+= 5.75
        icecreamsordered+= 1
    elif icecreamselection=="cookie dough":
        print("Adding cookie dough ice cream to order")
        order_cost+= 6.25
        icecreamsordered+= 1
    else:
        icecreamselection=input("Invalid selection. Please enter a valid flavor: ")
    
    sprinkles = input("Would you like sprinkles: Yes or No ").lower()

    if sprinkles == "yes":
        print("Adding sprinkles to ice cream. $0.50 added.")
        order.append(icecreamselection + " ice cream with sprinkles")
        order_cost += 0.50
    elif sprinkles == "no":
        print("Not adding sprinkles to ice cream.")
        order.append(icecreamselection + " ice cream")
    else:
        sprinkles = input("Invalid selection. Please enter yes or no. ")

print("\nYour Order:")
for item in order:
    print(item)
print("Total cost: $" + str(order_cost))
