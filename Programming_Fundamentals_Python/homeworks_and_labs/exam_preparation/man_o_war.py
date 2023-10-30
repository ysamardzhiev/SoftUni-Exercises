pirate_ship_status = [int(s) for s in input().split('>')]
warship_status = [int(s) for s in input().split('>')]
max_health_per_section = int(input())

pirate_ship_sunk = False
warship_sunk = False
command = input()
while command != 'Retire':
    commands = command.split()
    action = commands[0]
    if action == 'Fire':
        index = int(commands[1])
        damage = int(commands[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                warship_sunk = True
                break
    elif action == 'Defend':
        start_index = int(commands[1])
        end_index = int(commands[2])
        damage = int(commands[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for section_index in range(start_index, end_index + 1):
                pirate_ship_status[section_index] -= damage
                if pirate_ship_status[section_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    pirate_ship_sunk = True
                    break
            if pirate_ship_sunk:
                break
    elif action == 'Repair':
        index = int(commands[1])
        health = int(commands[2])
        if 0 <= index < len(pirate_ship_status) and pirate_ship_status[index] < max_health_per_section:
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_per_section:
                pirate_ship_status[index] = pirate_ship_status[index] - (pirate_ship_status[index] - max_health_per_section)
    elif action == 'Status':
        need_of_repair_sections = [s for s in pirate_ship_status if s < max_health_per_section * 0.2]
        print(f"{len(need_of_repair_sections)} sections need repair.")
    command = input()

if not warship_sunk and not pirate_ship_sunk:
    print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")