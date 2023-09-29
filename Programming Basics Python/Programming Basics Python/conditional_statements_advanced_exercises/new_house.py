type_flower = input()
flowers_count = int(input())
budget = int(input())

rose_price = flowers_count * 5
dahlia_price = flowers_count * 3.80
tulip_price = flowers_count * 2.80
narcissus_price = flowers_count * 3
gladiolus_price = flowers_count * 2.50
price = 0

if type_flower == 'Roses':
    if flowers_count > 80:
        price = rose_price - (rose_price * 0.10)
    else:
        price = rose_price
elif type_flower == 'Dahlias':
    if flowers_count > 90:
        price = dahlia_price - (dahlia_price * 0.15)
    else:
        price = dahlia_price
elif type_flower == 'Tulips':
    if flowers_count > 80:
        price = tulip_price - (tulip_price * 0.15)
    else:
        price = tulip_price
elif type_flower == 'Narcissus':
    if flowers_count < 120:
        price = narcissus_price + (narcissus_price * 0.15)
    else:
        price = narcissus_price
elif type_flower == 'Gladiolus':
    if flowers_count < 80:
        price = gladiolus_price + (gladiolus_price * 0.20)
    else:
        price = gladiolus_price

diff = abs(price - budget)

if price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")