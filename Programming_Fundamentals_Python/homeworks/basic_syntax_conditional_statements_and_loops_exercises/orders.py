number_of_orders = int(input())

total_price_for_the_coffee = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100 or not 1 <= days <= 31 or not 1 <= needed_capsules_per_day <= 2000:
        continue

    price_for_the_coffee = price_per_capsule * days * needed_capsules_per_day
    print(f"The price for the coffee is: ${price_for_the_coffee:.2f}")

    total_price_for_the_coffee += price_for_the_coffee

print(f"Total: ${total_price_for_the_coffee:.2f}")