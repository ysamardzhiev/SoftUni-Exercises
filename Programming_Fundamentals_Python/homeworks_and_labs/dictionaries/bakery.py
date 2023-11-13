stock = input().split()

foods = [stock[i] for i in range(len(stock)) if i % 2 == 0]
quantities = [int(stock[i]) for i in range(len(stock)) if i % 2]

print(dict(zip(foods, quantities)))