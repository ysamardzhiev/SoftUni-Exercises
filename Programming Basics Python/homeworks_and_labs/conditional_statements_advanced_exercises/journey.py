budget = float(input())
season = input()

price = 0
destination = ""
type_of_rest = ""

if season == 'summer':
    type_of_rest = 'Camp'
    if budget <= 100:
        price = budget * 0.70
        destination = 'Bulgaria'
    elif budget <= 1000:
        price = budget * 0.60
        destination = 'Balkans'
    elif budget > 1000:
        price = budget * 0.10
        destination = 'Europe'
        type_of_rest = 'Hotel'
elif season == 'winter':
    type_of_rest = 'Hotel'
    if budget <= 100:
        price = budget * 0.30
        destination = 'Bulgaria'
    elif budget <= 1000:
        price = budget * 0.20
        destination = 'Balkans'
    elif budget > 1000:
        price = budget * 0.10
        destination = 'Europe'

diff = abs(budget - price)

print(f'Somewhere in {destination}')
print(f'{type_of_rest} - {diff:.2f}')