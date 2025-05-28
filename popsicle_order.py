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
        order.append("special popsicle\n")
        order_cost += 6.00
        popsicles_ordered += 1
    elif popsicle_type == "mango":
        print("Adding mango popsicle to your order. $5.50 has been added to your total.")
        order.append("mango popsicle\n")
        order_cost += 5.50
        popsicles_ordered += 1
    elif popsicle_type == "chocolate":
        print("Adding chocolate popsicle to your order. $5.00 has been added to your total.")
        order.append("chocolate popsicle\n")
        order_cost += 5.00
        popsicles_ordered += 1
    elif popsicle_type == "strawberry":
        print("Adding strawberry popsicle to your order. $4.75 has been added to your total.")
        order.append("strawberry popsicle\n")
        order_cost += 4.75
        popsicles_ordered += 1
    elif popsicle_type == "cherry":
        print("Adding cherry popsicle to your order. $5.25 has been added to your total.")
        order.append("cherry popsicle\n")
        order_cost += 5.25
        popsicles_ordered += 1
    elif popsicle_type == "vanilla":
        print("Adding vanilla popsicle to your order. $4.50 has been added to your total.")
        order.append("vanilla popsicle\n")
        order_cost += 4.50
        popsicles_ordered += 1
    else:
        print("Invalid input. Please enter a valid option.\n")

print("\nYour order:\n" + "".join(order))
print("Total: $" + str(order_cost))
