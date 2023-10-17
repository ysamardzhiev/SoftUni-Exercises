items_with_prices = input().split('|')
budget = float(input())

clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50

current_budget = budget
bought_items = []

for current_item in items_with_prices:
    type_of_item, price = current_item.split('->')
    price = float(price)
    if type_of_item == 'Clothes':
        if price <= clothes_max_price and current_budget >= price:
            current_budget -= price
            bought_items.append(price)
    elif type_of_item == 'Shoes':
        if price <= shoes_max_price and current_budget >= price:
            current_budget -= price
            bought_items.append(price)
    elif type_of_item == 'Accessories':
        if price <= accessories_max_price and current_budget >= price:
            current_budget -= price
            bought_items.append(price)

increased_items = []

for item_price in bought_items:
    increased_price = item_price * (1 + 0.4)
    increased_items.append(increased_price)

profit = sum(increased_items) - sum(bought_items)
final_budget = profit + budget
train_ticket = 150

increased_items_as_str = []

for number in increased_items:
    increased_items_as_str.append(f'{number:.2f}')

print(' '.join(increased_items_as_str))
print(f'Profit: {profit:.2f}')
if final_budget >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')