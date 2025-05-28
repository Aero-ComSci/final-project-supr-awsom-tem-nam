order = []
order_cost = 0.00

# Popsicles
amount_of_popsicles = input("How many popsicles would you like? ")
while not amount_of_popsicles.isdigit() or int(amount_of_popsicles) < 1:
    print("Invalid input. Enter a positive integer.")
    amount_of_popsicles = input("How many popsicles would you like? ")

popsicles_ordered = 0
print("Popsicle Menu \n Pineapple: $4.00 \n Strawberry: $3.50 \n Chocolate: $3.50 \n Vanilla: $3.00 \n Cherry: $3.50 \n Mango: $4.00 \n Special Spongebob Flavor: $5.00")
while popsicles_ordered < int(amount_of_popsicles):
    popsicle_type = input("Which popsicle would you like? For spongebob flavor, type 'special': ").lower()
    if popsicle_type == "special":
        print("Adding special to your order. $5.00 has been added to your total.")
        order.append(popsicle_type)
        order_cost += 5.00
        popsicles_ordered += 1
    elif popsicle_type in ["pineapple", "mango"]:
        print("Adding " + popsicle_type + " popsicle to your order. $4.00 has been added to your total.")
        order.append(popsicle_type)
        order_cost += 4.00
        popsicles_ordered += 1
    elif popsicle_type in ["chocolate", "strawberry", "cherry"]:
        print("Adding " + popsicle_type + " popsicle to your order. $3.50 has been added to your total.")
        order.append(popsicle_type)
        order_cost += 3.50
        popsicles_ordered += 1
    elif popsicle_type == "vanilla":
        print("Adding vanilla popsicle to your order. $3.00 has been added to your total.")
        order.append(popsicle_type)
        order_cost += 3.00
        popsicles_ordered += 1
    else:
        print("Invalid input. Please enter a valid option.")

print(order)
print(order_cost)
