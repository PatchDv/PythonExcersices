foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item you want to add to your cart (q to quit): ")
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n--- Your Cart ---")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Total: ${total}")