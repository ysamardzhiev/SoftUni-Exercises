chrysanthemum_count = int(input())
roses_count = int(input())
tulip_count = int(input())
season = input()
festival = input()

price = 0

if season == 'Spring' or season == 'Summer':
    price = (2 * chrysanthemum_count) + (4.1 * roses_count) + (2.5 * tulip_count)
elif season == 'Autumn' or season == 'Winter':
    price = (3.75 * chrysanthemum_count) + (4.5 * roses_count) + (4.15 * tulip_count)

if festival == 'Y':
    price = price * (1 + 0.15)

if season == 'Spring':
    if tulip_count > 7:
        price = price * 0.95
elif season == 'Winter':
    if roses_count >= 10:
        price = price * 0.9

if (chrysanthemum_count + roses_count + tulip_count) > 20:
    price = price * 0.8

price = price + 2
print(f'{price:.2f}')
