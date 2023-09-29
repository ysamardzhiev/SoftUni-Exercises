budget = float(input())
season = input()

price = 0
car_class = ""

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        price = budget * 0.65
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        price = budget * 0.80
elif budget > 500:
    car_class = 'Luxury class'
    if season == 'Summer' or season == 'Winter':
        car = 'Jeep'
        price = budget * 0.90

print(f"{car_class}")
print(f"{car} - {price:.2f}")