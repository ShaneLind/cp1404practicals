"""
CP1404 - Practical
Shop Calculator
"""

# initial pseudocode:
# total = 0
# get number of items
# for i in range (0,num_items,1
#   get price of item
#   total_price = total_price + item_price
# if total_price > 100
#   total_price = total_price * 0.9
# print total_price

total_price = 0
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Reenter number of items: "))

for i in range(0, number_of_items, 1):
    item_price = float(input(f"Price of item {i + 1:}: $"))
    total_price = total_price + item_price

if total_price > 100:
    total_price = total_price * 0.9

print(f"The total price for {number_of_items} items is ${total_price:.2f}")
