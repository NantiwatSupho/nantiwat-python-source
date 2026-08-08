prices = []
print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)
print()
budget = int(input("Enter total budget: "))
print()
total = 0
bought = []
for i in range(6):
    if total+prices[i] <= budget:
        bought.append(prices[i])
        total += prices[i]
        print(f"Item {i+1} = {prices[i]} -> buy")
        print(f"Current total = {total}")
        print()
    else:
        print(f"Item {i+1} = {prices[i]} -> canot buy")
        print(f"Current total = {total}")
        print()
print(f"Bought item: {bought}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")