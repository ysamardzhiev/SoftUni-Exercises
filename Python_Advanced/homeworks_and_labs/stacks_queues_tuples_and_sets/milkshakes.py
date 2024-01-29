from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes_count = 0

while chocolates and cups_of_milk and milkshakes_count < 5:
    chocolate = chocolates.pop() if cups_of_milk[0] > 0 or chocolates[-1] <= 0 else 0
    cup_of_milk = cups_of_milk.popleft() if chocolate > 0 or cups_of_milk[0] <= 0 else 0

    if cup_of_milk <= 0:
        continue

    if chocolate == cup_of_milk:
        milkshakes_count += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)

print("Great! You made all the chocolate milkshakes needed!") if milkshakes_count == 5 else print("Not enough milkshakes.")
print(f'Chocolate: {", ".join(str(x) for x in chocolates) or "empty"}')
print(f'Milk: {", ".join(str(x) for x in cups_of_milk) or "empty"}')