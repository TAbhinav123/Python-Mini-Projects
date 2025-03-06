
menu = {
    "PIZZA" : 40,
    "Pasta" : 70,
    "Burger" : 130,
    "Coffee" : 40,
    "Juice" : 30
}

print("Welcome to ABHINAV Restaurant : ")
print("Please Select Any Of The Dishes ")
print("PIZZA: Rs40\nPasta: Rs70\nBurger: Rs130\nCoffee: Rs40\nJuice: Rs30 ")

order_total = 0

# First item order
item_1 = input("Enter the name of item you want to order: ").capitalize()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to the order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

# Asking for additional items
while True:
    another_order = input("Do you want to add another item? (Yes/No): ").capitalize()
    if another_order == "Yes":
        item_2 = input("Enter the name of the next item: ").capitalize()
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item {item_2} has been added to the order.")
        else:
            print(f"Ordered item {item_2} is not available.")
    elif another_order == "No":
        break
    else:
        print("Invalid input. Please answer 'Yes' or 'No'.")

print(f"Total amount of items to pay is Rs{order_total}")
