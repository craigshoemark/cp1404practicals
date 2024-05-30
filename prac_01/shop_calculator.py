# Shop Calculator
"""
get number_of_items
while number_of_items < 0
    print invalid message
    get number_of_items
for item in number_of_items
    get price_of_item
    total_price += price_of_item
if total_price > 100:
    discount = total_price * 0.10
    total_price = total_price - discount
print number_of_items, total_price
"""
total_price = 0
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter number of items: "))
for item in range(number_of_items):
    price_of_item = float(input("Enter price of item: "))
    total_price += price_of_item
if total_price > 100:
    discount = total_price * 0.10
    total_price = total_price - discount
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
