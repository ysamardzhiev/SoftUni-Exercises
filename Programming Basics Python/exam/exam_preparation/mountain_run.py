from math import floor

all_time_record = float(input())
distance = float(input())
time_seconds_in_1_meter = float(input())

must_climb = distance * time_seconds_in_1_meter
slow_down = floor((distance / 50)) * 30

total_time = must_climb + slow_down
diff = abs(total_time - all_time_record)

if total_time < all_time_record:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')