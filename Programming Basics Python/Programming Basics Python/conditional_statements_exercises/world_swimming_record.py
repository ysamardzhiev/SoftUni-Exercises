from math import floor
record = float(input())
meters = float(input())
seconds_for_meter = float(input())

new_record = meters * seconds_for_meter
water_resistance = floor(meters / 15) * 12.5
total_time = new_record + water_resistance
diff = abs(total_time - record)

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")