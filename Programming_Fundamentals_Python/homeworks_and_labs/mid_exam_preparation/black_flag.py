days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_gain = 0

for day in range(1, days_of_plunder + 1):
    total_gain += daily_plunder
    if day % 3 == 0:
        total_gain += daily_plunder * 0.5
    if day % 5 == 0:
        total_gain -= total_gain * 0.3

percentage = (total_gain / expected_plunder) * 100
if total_gain >= expected_plunder:
    print(f"Ahoy! {total_gain:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")