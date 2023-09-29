season = input()
km_per_month = float(input())

price = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price = 0.75 * km_per_month
    elif season == 'Summer':
        price = 0.90 * km_per_month
    elif season == 'Winter':
        price = 1.05 * km_per_month
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price = 0.95 * km_per_month
    elif season == 'Summer':
        price = 1.10 * km_per_month
    elif season == 'Winter':
        price = 1.25 * km_per_month
elif 10000 < km_per_month <= 20000:
    price = 1.45 * km_per_month

total_price = (price * 4) * 0.90
print(f'{total_price:.2f}')