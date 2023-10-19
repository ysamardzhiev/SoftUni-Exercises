def total_order(product: str, quantity: int) -> float:
    if product == 'coffee':
        return quantity * 1.50
    elif product == 'coke':
        return quantity * 1.40
    elif product == 'water':
        return quantity * 1
    elif product == 'snacks':
        return quantity * 2


type_of_product = input()
quantity = int(input())
total_price = total_order(type_of_product, quantity)
print(f'{total_price:.2f}')
