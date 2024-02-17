from collections import deque

money = [int(el) for el in input().split()]
prices = deque(int(el) for el in input().split())

eaten_food = 0

while money and prices:
    current_amount = money.pop()
    price = prices.popleft()

    if current_amount < price:
        continue

    elif current_amount > price:
        if money:
            money[-1] += current_amount - price

    eaten_food += 1

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif eaten_food:
    if eaten_food == 1:
        print(f"Henry ate: {eaten_food} food.")
    else:
        print(f"Henry ate: {eaten_food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")