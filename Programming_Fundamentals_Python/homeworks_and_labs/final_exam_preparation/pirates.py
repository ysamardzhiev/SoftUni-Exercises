def add_cities(cities, city, population, gold):
    if city not in cities.keys():
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += int(population)
    cities[city]['gold'] += int(gold)


def action_plunder(cities, town, people, gold):
    cities[town]['population'] -= people
    cities[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
        cities.pop(town)
        print(f"{town} has been wiped off the map!")


def action_prosper(cities, town, gold):
    if gold >= 0:
        cities[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    else:
        print(f"Gold added cannot be a negative number!")


cities = {}

command = input()
while command != 'Sail':
    city, population, gold = command.split('||')
    add_cities(cities, city, population, gold)
    command = input()

command = input()
while command != 'End':
    commands = command.split('=>')
    if commands[0] == 'Plunder':
        town, people, gold = commands[1], int(commands[2]), int(commands[3])
        action_plunder(cities, town, people, gold)
    elif commands[0] == 'Prosper':
        town, gold = commands[1], int(commands[2])
        action_prosper(cities, town, gold)
    command = input()
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, info in cities.items():
        print(f"{city} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")