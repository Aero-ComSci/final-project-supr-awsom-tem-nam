order = []
order_cost = 0.00

amount_of_boba = input("How many boba drinks would you like? ")
while not amount_of_boba.isdigit() or int(amount_of_boba) < 1:
    print("Invalid input. Enter a positive integer.")
    amount_of_boba = input("How many boba drinks would you like? ")

boba_ordered = 0
print("Boba Menu \n Taro Milk Tea: $6.50 \n Thai Milk Tea: $6.00 \n Brown Sugar Milk Tea: $6.50 \n Mango Milk Tea: $5.50 \n Strawberry Milk Tea: $5.50")
print("Toppings ($1.25 each): Honeydew Boba, Crushed Oreos, Lychee Jelly")
print("Complimentary: Tapioca Pearls")

while boba_ordered < int(amount_of_boba):
    boba_type = input("Which boba would you like? ").lower()
    
    if boba_type == "taro milk tea":
        print("Adding taro milk tea to your order. $6.50 has been added to your total.")
        order.append(boba_type)
        order_cost += 6.50
        boba_ordered += 1
    elif boba_type in ["thai milk tea", "brown sugar milk tea"]:
        print("Adding " + boba_type + " to your order. $6.00 has been added to your total.")
        order.append(boba_type)
        order_cost += 6.00
        boba_ordered += 1
    elif boba_type in ["mango milk tea", "strawberry milk tea"]:
        print("Adding " + boba_type + " to your order. $5.50 has been added to your total.")
        order.append(boba_type)
        order_cost += 5.50
        boba_ordered += 1
    else:
        print("Invalid input. Please enter a valid option.")
