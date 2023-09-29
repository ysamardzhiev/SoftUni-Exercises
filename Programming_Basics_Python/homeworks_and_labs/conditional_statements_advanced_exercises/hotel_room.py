month = input()
nights_count = int(input())

price_studio = 0
price_apart = 0

if month == 'May' or month == 'October':
    price_studio = 50 * nights_count
    price_apart = 65 * nights_count
    if 7 < nights_count <= 14:
        price_studio = price_studio * 0.95
    elif nights_count > 14:
        price_studio = price_studio * 0.70
        price_apart = price_apart * 0.90
elif month == 'June' or month == 'September':
    price_studio = 75.20 * nights_count
    price_apart = 68.70 * nights_count
    if nights_count > 14:
        price_studio = price_studio * 0.80
        price_apart = price_apart * 0.90
elif month == 'July' or month == 'August':
    price_studio = 76 * nights_count
    price_apart = 77 * nights_count
    if nights_count > 14:
        price_apart = price_apart * 0.90

print(f"Apartment: {price_apart:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")