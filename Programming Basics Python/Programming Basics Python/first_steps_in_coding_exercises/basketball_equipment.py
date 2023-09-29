annual_tax_per_year = int(input())

price_for_sneakers = annual_tax_per_year - (annual_tax_per_year * 0.40)
price_for_kit = price_for_sneakers - (price_for_sneakers * 0.20)
price_for_ball = 1 / 4 * price_for_kit
price_for_accessories = 1 / 5 * price_for_ball

total_price = price_for_accessories + price_for_kit + price_for_ball + price_for_sneakers + annual_tax_per_year

print(total_price)