order = []
order_cost = 0.00

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
        order.append(boba_type + " boba with " + toppings + "\n")
        order_cost += 1.25
    elif toppings == "none":
        print("No extra toppings added.")
        order.append(boba_type + " boba with tapioca pearls \n")
    else:
        toppings = input("Invalid input. Enter a valid topping or 'none'. ")

print("\nYour order:\n" + "".join(order))
print("Total: $" + str(order_cost))
