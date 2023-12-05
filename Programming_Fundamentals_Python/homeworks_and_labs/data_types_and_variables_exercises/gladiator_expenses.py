lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_count = 0
broken_sword_count = 0
broken_shield_count = 0
broken_armor_count = 0

for current_fight in range(1, lost_fights_count + 1):
    if current_fight % 2 == 0:
        broken_helmet_count += 1
    if current_fight % 3 == 0:
        broken_sword_count += 1
    if current_fight % 3 == 0 and current_fight % 2 == 0:
        broken_shield_count += 1
        if broken_shield_count % 2 == 0:
            broken_armor_count += 1

expenses = (broken_helmet_count * helmet_price) + (broken_sword_count * sword_price) + \
           (broken_shield_count * shield_price) + (broken_armor_count * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")