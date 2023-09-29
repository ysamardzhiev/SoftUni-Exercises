young_bikers_count = int(input())
old_bikers_count = int(input())
race_type = input()

price_juniors = 0
price_seniors = 0

if race_type == 'trail':
    price_juniors = 5.5 * young_bikers_count
    price_seniors = 7 * old_bikers_count
elif race_type == 'cross-country':
    price_juniors = 8 * young_bikers_count
    price_seniors = 9.5 * old_bikers_count
    if young_bikers_count + old_bikers_count >= 50:
        price_juniors = (8 * young_bikers_count) * 0.75
        price_seniors = (9.5 * old_bikers_count) * 0.75
elif race_type == 'downhill':
    price_juniors = 12.25 * young_bikers_count
    price_seniors = 13.75 * old_bikers_count
elif race_type == 'road':
    price_juniors = 20 * young_bikers_count
    price_seniors = 21.5 * old_bikers_count

total_sum = (price_juniors + price_seniors) * 0.95
print(f'{total_sum:.2f}')