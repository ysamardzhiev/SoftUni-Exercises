from collections import deque

food_quantity = int(input())

orders = deque([int(order) for order in input().split()])
biggest_order = max(orders)

for order in orders.copy():
    if order <= food_quantity:
        food_quantity -= order
        orders.popleft()
    else:
        break
print(biggest_order)
if orders:
    print('Orders left:', *orders)
else:
    print('Orders complete')