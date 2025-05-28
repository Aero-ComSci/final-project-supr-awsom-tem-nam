order = []
order_cost = 0.00

amount_of_boba = input("How many boba drinks would you like? ")
while not amount_of_boba.isdigit() or int(amount_of_boba) < 1:
    print("Invalid input. Enter a positive integer.")
    amount_of_boba = input("How many boba drinks would you like? ")

boba_ordered = 0
menu_text = "Boba Menu\n Taro Milk Tea: $7.00\n Thai Milk Tea: $6.50\n Brown Sugar Milk Tea: $7.25\n Mango Milk Tea: $6.75\n Strawberry Milk Tea: $6.75\nToppings ($1.25 each): Honeydew Boba, Crushed Oreos, Lychee Jelly\nComplimentary: Tapioca Pearls"
print(menu_text)

while boba_ordered < int(amount_of_boba):
    boba_type = input("Which boba would you like? ").lower()
    
    if boba_type == "taro":
        print("Adding taro milk tea to your order. $7.00 has been added to your total.")
        order.append("taro milk tea\n")
        order_cost += 7.00
        boba_ordered += 1
    elif boba_type == "thai":
        print("Adding thai milk tea to your order. $6.50 has been added to your total.")
        order.append("thai milk tea\n")
        order_cost += 6.50
        boba_ordered += 1
    elif boba_type == "brown sugar":
        print("Adding brown sugar milk tea to your order. $7.25 has been added to your total.")
        order.append("brown sugar milk tea\n")
        order_cost += 7.25
        boba_ordered += 1
    elif boba_type == "mango":
        print("Adding mango milk tea to your order. $6.75 has been added to your total.")
        order.append("mango milk tea\n")
        order_cost += 6.75
        boba_ordered += 1
    elif boba_type == "strawberry":
        print("Adding strawberry milk tea to your order. $6.75 has been added to your total.")
        order.append("strawberry milk tea\n")
        order_cost += 6.75
        boba_ordered += 1
    else:
        print("Invalid input. Please enter a valid option.")

print("\nYour order:\n" + "".join(order))

print("Total: $" + str(order_cost))
   toppings = input("Would you like any toppings? (Honeydew Boba, Crushed Oreos, Lychee Jelly) Type 'none' if no toppings: ").lower()
    if toppings in ["honeydew boba", "crushed oreos", "lychee jelly"]:
        print("Adding " + toppings + " to your order. $1.25 has been added to your total.")
        order.append(toppings + "\n")
        order_cost += 1.25
    elif toppings == "none":
        print("No extra toppings added.")
    else:
        print("Invalid input. No extra toppings added.")

    print("Complimentary tapioca pearls have been added to your order!\n")

print("Your order:\n" + "".join(order))
print("Total: $" + str(order_cost))
