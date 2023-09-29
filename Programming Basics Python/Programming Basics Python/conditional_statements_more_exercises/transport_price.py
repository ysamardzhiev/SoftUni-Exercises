kilometers = int(input())
day_or_night = input()
price = 0

if day_or_night == 'day':
    if kilometers < 20:
        price = 0.70 + (kilometers * 0.79)
    elif 20 <= kilometers < 100:
        price = kilometers * 0.09
    elif kilometers >= 100:
        price = kilometers * 0.06
elif day_or_night == 'night':
    if kilometers < 20:
        price = 0.70 + (kilometers * 0.90)
    elif 20 <= kilometers < 100:
        price = kilometers * 0.09
    elif kilometers >= 100:
        price = kilometers * 0.06

print(f'{price:.2f}')
