order = []
order_cost = 0.00

amount_of_popsicles = input("How many popsicles would you like? ")
while not amount_of_popsicles.isdigit() or int(amount_of_popsicles) < 1:
    print("Invalid input. Enter a positive integer.")
    amount_of_popsicles = input("How many popsicles would you like? ")

popsicles_ordered = 0
print("Popsicle Menu \n Pineapple: $4.00 \n Strawberry: $3.50 \n Chocolate: $3.50 \n Vanilla: $3.00 \n Cherry: $3.50 \n Mango: $4.00 \n Special Spongebob Flavor: $5.00")
while popsicles_ordered < amount_of_popsicles:
    popsicle_type = input("Which popsicle would you like? ")
    if popsicle_type == ""
