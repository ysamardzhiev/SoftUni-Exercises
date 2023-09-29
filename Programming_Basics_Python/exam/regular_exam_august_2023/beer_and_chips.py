from math import ceil

name = input()
budget = float(input())
beers_count = int(input())
chips_count = int(input())

total_beer_price = beers_count * 1.20
price_for_chips = total_beer_price * 0.45
total_chips_price = ceil(price_for_chips * chips_count)

total_amount = total_chips_price + total_beer_price

diff = abs(total_amount - budget)
if total_amount <= budget:
    print(f'{name} bought a snack and has {diff:.2f} leva left.')
else:
    print(f'{name} needs {diff:.2f} more leva!')