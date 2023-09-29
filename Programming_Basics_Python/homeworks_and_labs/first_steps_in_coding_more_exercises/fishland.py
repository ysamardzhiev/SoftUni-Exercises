mackerel_price = float(input())
sprat_price = float(input())
bonito_count = float(input())
scad_count = float(input())
mussel_count = int(input())

bonito_price = mackerel_price + (mackerel_price * 0.60)
bonito_total = bonito_price * bonito_count
scad_price = sprat_price + (sprat_price * 0.80)
scad_total = scad_price * scad_count
mussel_total = mussel_count * 7.50

total_price = bonito_total + scad_total + mussel_total
print(f'{total_price:.2f}')
