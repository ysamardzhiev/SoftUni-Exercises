products_and_quantities = input().split()
products = input().split()

stock = {}

for i in range(0, len(products_and_quantities), 2):
    product = products_and_quantities[i]
    quantity = products_and_quantities[i + 1]
    stock[product] = int(quantity)

for current_product in products:
    if current_product in stock:
        print(f'We have {stock.get(current_product)} of {current_product} left')
    else:
        print(f"Sorry, we don't have {current_product}")