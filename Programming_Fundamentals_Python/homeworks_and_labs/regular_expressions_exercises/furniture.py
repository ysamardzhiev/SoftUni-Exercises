import re

total_cost = 0
bought_furniture = []

command = input()
while command != 'Purchase':
    purchase_info = command
    valid_item = re.search(r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)", purchase_info)
    if valid_item:
        furniture, price, quantity = valid_item.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')