from collections import deque

food_quantity = int(input())

orders = deque([int(order) for order in input().split()])
biggest_order = max(orders)

while orders:
    current_order = orders.popleft()
    if current_order <= food_quantity:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        break
print(biggest_order)
if orders:
    print('Orders left:', *orders)
else:
    print('Orders complete')