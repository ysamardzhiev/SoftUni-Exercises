stock = {}

command = input()
while command != 'statistics':
    product, quantity = command.split(': ')
    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)
    command = input()

print('Products in stock:')
for k, v in stock.items():
    print(f'- {k}: {v}')
print(f'Total Products: {len(stock)}\n'
      f'Total Quantity: {sum(stock.values())}')