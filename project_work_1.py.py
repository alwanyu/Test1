#Description: question 1, 2, 4, 5
#A vending machine program that allows users to choose snacks/drinks, view prices, and print a receipt.
#Key Skills: loops, input(), conditionals, lists/dictionaries, sum(), formatting
#Python Code:
items = {"1": ("Chips", 20), "2": ("Soda", 15), "3": ("Water", 10)}
cart = []
print("Welcome to the vending machine!")
for k, v in items.items():
    print(f"{k}. {v[0]} - ${v[1]}")
while True:
    choice = input("Choose item number (or 'done'): ")
    if choice.lower() == "done":
        break
    elif choice in items:
        cart.append(items[choice])
    else:
        print("Invalid choice.")
print("\nReceipt:")
total = sum(price for _, price in cart)
for item, price in cart:
    print(f"{item} - ${price}")
print(f"Total: ${total}")


#Description:
#A grocery checkout system using a dictionary of items and prices.
#Key Skills: dictionaries, loops, input(), math operations, error handling
#Python Code:
groceries = {"apple": 5, "banana": 3, "milk": 10}
cart = {}
while True:
    item = input("Add item or 'checkout': ").lower()
    if item == "checkout":
        break
    if item in groceries:
        qty = int(input(f"How many {item}s? "))
        cart[item] = cart.get(item, 0) + qty
    else:
        print("Item not found.")
print("\nReceipt:")
total = 0
for item, qty in cart.items():
    subtotal = groceries[item] * qty
    print(f"{item} x{qty} = ${subtotal}")
    total += subtotal
print(f"Total: ${total}")

#Description:
#Simulate booking movie tickets and calculating total cost.
#Key Skills: nested dictionaries, loops, input(), math operations
#Python Code:
movies = {
    "1": {"title": "Avatar 2", "price": 12},
    "2": {"title": "Oppenheimer", "price": 15}
}
total_cost = 0
while True:
    for k, v in movies.items():
        print(f"{k}. {v['title']} - ${v['price']}")
    choice = input("Choose movie or 'no': ")
    if choice == "no":
        break
    num = int(input("Tickets: "))
    total_cost += movies[choice]["price"] * num
print(f"Total booking cost: ${total_cost}")
