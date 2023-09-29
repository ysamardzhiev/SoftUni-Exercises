from math import ceil, floor
days_away = int(input())
left_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_needed_food = days_away * dog_food_per_day
cat_needed_food = days_away * cat_food_per_day
turtle_needed_food = (days_away * turtle_food_per_day) / 1000
total_food = dog_needed_food + cat_needed_food + turtle_needed_food
diff = abs(total_food - left_food)

if total_food >= left_food:
    print(f"{ceil(diff)} more kilos of food are needed.")
else:
    print(f"{floor(diff)} kilos of food left.")