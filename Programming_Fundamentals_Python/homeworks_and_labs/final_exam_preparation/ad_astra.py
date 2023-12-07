import re

food_info = input()

total_cal = 0

matches = re.findall(r"(#|\|)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1", food_info)

for match in matches:
    total_cal += int(match[3])

days_to_last = total_cal // 2000
print(f'You have food to last you for: {days_to_last} days!')
for match in matches:
    item, expiration_date, calories = match[1], match[2], match[3]
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")