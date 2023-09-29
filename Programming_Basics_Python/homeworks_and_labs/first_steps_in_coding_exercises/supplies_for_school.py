total_pens = int(input())
total_markers = int(input())
liters_of_bleach = int(input())
discount_percentage = int(input())

price_of_pens = total_pens * 5.80
price_of_markers = total_markers * 7.20
price_of_bleach = liters_of_bleach * 1.20
total_price_without_discount = price_of_pens + price_of_markers + price_of_bleach
total_price = total_price_without_discount - (total_price_without_discount * discount_percentage / 100)

print(total_price)