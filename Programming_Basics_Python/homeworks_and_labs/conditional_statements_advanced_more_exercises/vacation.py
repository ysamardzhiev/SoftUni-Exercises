budget = float(input())
season = input()

price = 0

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.8
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.6
elif budget > 3000:
    accommodation = 'Hotel'
    price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f"{location} - {accommodation} - {price:.2f}")