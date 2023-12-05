days_of_adventure = int(input())
players_count = int(input())
group_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())

total_water = days_of_adventure * players_count * water_per_day_for_one_person
total_food = days_of_adventure * players_count * food_per_day_for_one_person

for day in range(1, days_of_adventure + 1):
    energy_loss_amount = float(input())
    group_energy -= energy_loss_amount
    if group_energy <= 0:
        break
    if day % 2 == 0:
        group_energy = group_energy * (1 + 0.05)
        total_water = total_water * (1 - 0.30)
    if day % 3 == 0:
        group_energy = group_energy * (1 + 0.10)
        total_food -= total_food / players_count

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")