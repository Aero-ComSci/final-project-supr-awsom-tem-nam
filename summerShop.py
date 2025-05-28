order = []
order_cost = 0.00

amount_of_popsicles = input("How many popsicles would you like? ")
while not amount_of_popsicles.isdigit() or int(amount_of_popsicles) < 1:
    print("Invalid input. Enter a positive integer. ")
    amount_of_popsicles = input("How many popsicles would you like? ")

popsicles_ordered = 0
print("Popsicle Menu\n Strawberry: $4.75\n Chocolate: $5.00\n Vanilla: $4.50\n Cherry: $5.25\n Mango: $5.50\n Special Spongebob Flavor: $6.00\n")

while popsicles_ordered < int(amount_of_popsicles):
    popsicle_type = input("Which popsicle would you like? For Spongebob flavor, type 'special': ").lower()
    if popsicle_type == "special":
        print("Adding special to your order. $6.00 has been added to your total.")
        order.append("special popsicle")
        order_cost += 6.00
        popsicles_ordered += 1
    elif popsicle_type == "mango":
        print("Adding mango popsicle to your order. $5.50 has been added to your total.")
        order.append("mango popsicle")
        order_cost += 5.50
        popsicles_ordered += 1
    elif popsicle_type == "chocolate":
        print("Adding chocolate popsicle to your order. $5.00 has been added to your total.")
        order.append("chocolate popsicle")
        order_cost += 5.00
        popsicles_ordered += 1
    elif popsicle_type == "strawberry":
        print("Adding strawberry popsicle to your order. $4.75 has been added to your total.")
        order.append("strawberry popsicle")
        order_cost += 4.75
        popsicles_ordered += 1
    elif popsicle_type == "cherry":
        print("Adding cherry popsicle to your order. $5.25 has been added to your total.")
        order.append("cherry popsicle")
        order_cost += 5.25
        popsicles_ordered += 1
    elif popsicle_type == "vanilla":
        print("Adding vanilla popsicle to your order. $4.50 has been added to your total.")
        order.append("vanilla popsicle")
        order_cost += 4.50
        popsicles_ordered += 1
    else:
        print("Invalid input. Please enter a valid option.\n")

amount_of_boba = input("How many boba drinks would you like? ")
while not amount_of_boba.isdigit() or int(amount_of_boba) < 1:
    print("Invalid input. Enter a positive integer.")
    amount_of_boba = input("How many boba drinks would you like? ")

boba_ordered = 0
menu_text = "Boba Menu\n Taro : $7.00\n Thai : $6.50\n Brown Sugar : $7.25\n Mango : $6.75\n Strawberry : $6.75\n"
print(menu_text)

while boba_ordered < int(amount_of_boba):
    boba_type = input("Which boba would you like? ").lower()
    
    if boba_type == "taro":
        print("Adding taro to your order. $7.00 has been added to your total.")
        order_cost += 7.00
        boba_ordered += 1
    elif boba_type == "thai":
        print("Adding thai to your order. $6.50 has been added to your total.")
        order_cost += 6.50
        boba_ordered += 1
    elif boba_type == "brown sugar":
        print("Adding brown sugar to your order. $7.25 has been added to your total.")
        order_cost += 7.25
        boba_ordered += 1
    elif boba_type == "mango":
        print("Adding mango to your order. $6.75 has been added to your total.")
        order_cost += 6.75
        boba_ordered += 1
    elif boba_type == "strawberry":
        print("Adding strawberry to your order. $6.75 has been added to your total.")
        order_cost += 6.75
        boba_ordered += 1
    else:
        boba_type = input("Invalid input. Please enter a valid option.")
    
    toppings = input("Would you like any toppings? (Honeydew Boba, Crushed Oreos, Lychee Jelly) Type 'none' if no toppings (complimentary tapioca pearls!): ").lower()
    if toppings in ["honeydew boba", "crushed oreos", "lychee jelly"]:
        print("Adding " + toppings + " to your order. $1.25 has been added to your total.")
        order.append(boba_type + " boba with " + toppings)
        order_cost += 1.25
    elif toppings == "none":
        print("No extra toppings added.")
        order.append(boba_type + " boba with tapioca pearls")
    else:
        toppings = input("Invalid input. Enter a valid topping or 'none'. ")

icecreamamount = input("How many ice creams would you like to order? ")
while not icecreamamount.isdigit() or int(icecreamamount) < 1:
    print("Enter a valid number for ice cream count")
    icecreamamount = input("How many ice creams would you like to order? ")

icecreamsordered = 0
while icecreamsordered < int(icecreamamount):
    print("Ice Cream Menu \n Chocolate: $4.50 \n Strawberry: $5.25 \n Butter Pecan: $5.50 \n Vanilla: $5.75 \n Cookie Dough: $6.25 ")

    icecreamselection = input("What ice cream would you like? ").lower()

    if icecreamselection == "chocolate":
        print("Adding chocolate ice cream to order")
        order_cost += 4.50
        icecreamsordered += 1
    elif icecreamselection == "strawberry":
        print("Adding strawberry ice cream to order")
        order_cost += 5.25
        icecreamsordered += 1
    elif icecreamselection == "butter pecan":
        print("Adding butter peacan ice cream to order")
        order_cost += 5.50
        icecreamsordered += 1
    elif icecreamselection == "vanilla":
        print("Adding vanilla ice cream to order")
        order_cost += 5.75
        icecreamsordered += 1
    elif icecreamselection == "cookie dough":
        print("Adding cookie dough ice cream to order")
        order_cost += 6.25
        icecreamsordered += 1
    else:
        icecreamselection = input("Invalid selection. Please enter a valid flavor: ")
    
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
print("\nTotal cost: $" + str(order_cost))
