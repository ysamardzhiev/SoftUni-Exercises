travel_route = input().split('||')
initial_fuel = int(input())
initial_ammunition = int(input())

total_fuel = initial_fuel
total_ammunition = initial_ammunition

for command in travel_route:
    commands = command.split()
    type_of_command = commands[0]
    if type_of_command == 'Travel':
        light_years = int(commands[1])
        if total_fuel >= light_years:
            total_fuel -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break
    elif type_of_command == 'Enemy':
        enemy_armor = int(commands[1])
        if total_ammunition >= enemy_armor:
            total_ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            if total_fuel > enemy_armor:
                total_fuel -= 2 * enemy_armor  # Not sure
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif type_of_command == 'Repair':
        fuel_and_ammunition = int(commands[1])
        total_fuel += fuel_and_ammunition
        total_ammunition += 2 * fuel_and_ammunition
        print(f"Ammunitions added: {fuel_and_ammunition * 2}.\n"
              f"Fuel added: {fuel_and_ammunition}.")
    elif type_of_command == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break