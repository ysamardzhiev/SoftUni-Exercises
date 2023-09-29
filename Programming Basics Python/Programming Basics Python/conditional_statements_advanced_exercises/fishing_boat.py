group_budget = int(input())
season = input()
fishermen_count = int(input())

price = 0

if season == 'Spring':
    price = 3000
    if fishermen_count <= 6:
        price = price * 0.90
    elif 7 <= fishermen_count <= 11:
        price = price * 0.85
    elif fishermen_count >= 12:
        price = price * 0.75
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if fishermen_count <= 6:
        price = price * 0.90
    elif 7 <= fishermen_count <= 11:
        price = price * 0.85
    elif fishermen_count >= 12:
        price = price * 0.75
elif season == 'Winter':
    price = 2600
    if fishermen_count <= 6:
        price = price * 0.90
    elif 7 <= fishermen_count <= 11:
        price = price * 0.85
    elif fishermen_count >= 12:
        price = price * 0.75

if fishermen_count % 2 == 0:
    if not season == 'Autumn':
        price = price * 0.95

diff = abs(price - group_budget)

if group_budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
