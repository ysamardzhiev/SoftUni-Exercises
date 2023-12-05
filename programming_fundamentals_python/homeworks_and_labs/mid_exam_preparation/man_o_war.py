def main():
    pirate_ship_status = [int(s) for s in input().split('>')]
    warship_status = [int(s) for s in input().split('>')]
    max_health = int(input())

    command = input()
    while command != 'Retire':
        commands = command.split()
        action = commands[0]
        if action == 'Fire':
            index = int(commands[1])
            damage = int(commands[2])
            fire_action(warship_status, index, damage)
        elif action == 'Defend':
            start_index = int(commands[1])
            end_index = int(commands[2])
            damage = int(commands[3])
            defend_action(pirate_ship_status, start_index, end_index, damage)
        elif action == 'Repair':
            index = int(commands[1])
            health = int(commands[2])
            repair_action(pirate_ship_status, index, health, max_health)
        elif action == 'Status':
            status_action(pirate_ship_status, max_health)
        command = input()

    print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")


def fire_action(warship, index, damage):
    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()


def defend_action(pirate_ship, start_index, end_index, damage):
    if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
        for section_index in range(start_index, end_index + 1):
            pirate_ship[section_index] -= damage
            if pirate_ship[section_index] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()


def repair_action(pirate_ship, index, health, max_health):
    if 0 <= index < len(pirate_ship) and pirate_ship[index] < max_health:
        pirate_ship[index] = min(pirate_ship[index] + health, max_health)


def status_action(pirate_ship, max_health):
    need_of_repair_sections = [s for s in pirate_ship if s < max_health * 0.2]
    print(f"{len(need_of_repair_sections)} sections need repair.")


main()