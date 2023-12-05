number_of_pouring_times = int(input())

water_tank_capacity = 255
total_poured_water = 0

for _ in range(number_of_pouring_times):
    current_liters_of_water_poured = int(input())
    total_poured_water += current_liters_of_water_poured

    if total_poured_water > water_tank_capacity:
        print("Insufficient capacity!")
        total_poured_water -= current_liters_of_water_poured
print(total_poured_water)