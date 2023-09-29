budget_movie = float(input())
extra_count = int(input())
price_for_outfit_per_extra = float(input())

decor = budget_movie * 0.10
outfit = price_for_outfit_per_extra * extra_count

if extra_count > 150:
    outfit = outfit - (outfit * 0.10)

final_price = decor + outfit
diff = abs(budget_movie - final_price)

if final_price > budget_movie:
    print("Not enough money!")
    print(f'Wingard needs {diff:.2f} leva more.')
elif final_price <= budget_movie:
    print('Action!')
    print(f"Wingard starts filming with {diff:.2f} leva left.")
