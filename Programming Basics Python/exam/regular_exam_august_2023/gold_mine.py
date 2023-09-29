locations_count = int(input())


for i in range(locations_count):
    expected_quantity_per_day = float(input())
    days_count = int(input())
    avg_gold_gained = 0
    for j in range(days_count):
        gained_quantity_per_day = float(input())
        avg_gold_gained += gained_quantity_per_day
    avg_gold_gained = avg_gold_gained / days_count

    if avg_gold_gained >= expected_quantity_per_day:
        print(f'Good job! Average gold per day: {avg_gold_gained:.2f}.')
    else:
        diff = abs(avg_gold_gained - expected_quantity_per_day)
        print(f'You need {diff:.2f} gold.')
