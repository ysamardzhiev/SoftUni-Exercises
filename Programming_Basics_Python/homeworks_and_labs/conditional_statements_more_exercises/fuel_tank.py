type_fuel = input().lower()
fuel_liters = int(input())

if type_fuel == 'diesel' or type_fuel == 'gasoline' or type_fuel == 'gas':
    if fuel_liters >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")