orders = {}

command = input()
while command != 'buy':
    product, price, quantity = command.split()
    if product not in orders.keys():
        orders[product] = {'price': float(price), 'quantity': int(quantity)}
    else:
        orders[product]['price'] = float(price)
        orders[product]['quantity'] += int(quantity)
    command = input()

for product, product_info in orders.items():
    total_price = product_info['price'] * product_info['quantity']
    print(f"{product} -> {total_price:.2f}")