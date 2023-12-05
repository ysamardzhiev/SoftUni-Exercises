budget = float(input())
price_for_1kg_flour = float(input())

pack_of_eggs_price = price_for_1kg_flour * 0.75
price_for_1l_milk = price_for_1kg_flour * (1 + 0.25)

total_product_price = price_for_1kg_flour + pack_of_eggs_price + (price_for_1l_milk / 4)

colored_eggs_count = 0
loaf_counter = 0

while budget >= total_product_price:
    loaf_counter += 1
    budget -= total_product_price
    colored_eggs_count += 3

    if loaf_counter % 3 == 0:
        colored_eggs_count -= loaf_counter - 2

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs_count} eggs "
      f"and {budget:.2f}BGN left.")
