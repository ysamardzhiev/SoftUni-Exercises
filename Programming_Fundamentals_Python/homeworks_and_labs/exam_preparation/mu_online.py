def main():
    dungeon_rooms = input().split('|')

    health = 100
    bitcoins = 0

    for current_room in dungeon_rooms:
        commands = current_room.split()
        action = commands[0]
        if action == 'potion':
            heal_amount = int(commands[1])
            health = action_potion(health, heal_amount)
        elif action == 'chest':
            bitcoins_amount = int(commands[1])
            bitcoins = action_chest(bitcoins, bitcoins_amount)
        else:
            attack = int(commands[1])
            current_room_index = dungeon_rooms.index(current_room)
            health = action_fight(health, attack, action, current_room_index)

    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


def action_potion(health, heal):
    current_health = health
    health = min(health + heal, 100)
    if health < 100:
        heal_amount = heal
    else:
        heal_amount = health - current_health
    print(f"You healed for {heal_amount} hp.")
    print(f"Current health: {health} hp.")
    return health


def action_chest(current_bitcoins, bitcoins):
    current_bitcoins += bitcoins
    print(f"You found {bitcoins} bitcoins.")
    return current_bitcoins


def action_fight(health, attack, monster, room):
    health -= attack
    if health <= 0:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {room + 1}")
        exit()
    else:
        print(f"You slayed {monster}.")
    return health


main()