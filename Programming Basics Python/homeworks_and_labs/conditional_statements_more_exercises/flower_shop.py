from math import floor, ceil
magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

order_total = (magnolias_count * 3.25) + (hyacinths_count * 4) + (roses_count * 3.50) + (cactus_count * 8)
tax = order_total * 0.05
order_after_tax = order_total - tax
diff = abs(order_after_tax - gift_price)

if order_after_tax >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")