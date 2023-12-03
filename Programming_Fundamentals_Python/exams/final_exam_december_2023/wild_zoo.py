animals = {}
areas = {}

command = input()
while command != 'EndDay':
    action, animal_data = command.split(': ')
    if action == 'Add':
        animal, needed_food, area = animal_data.split('-')
        if animal not in animals.keys():
            animals[animal] = [0, area]
            if area not in areas:
                areas[area] = 0
            areas[area] += 1
        animals[animal][0] += int(needed_food)
    elif action == 'Feed':
        animal, food = animal_data.split('-')
        if animal in animals.keys():
            animals[animal][0] -= int(food)
            if animals[animal][0] <= 0:
                print(f"{animal} was successfully fed")
                areas[animals[animal][1]] -= 1
                animals.pop(animal)
    command = input()

print('Animals:')
for animal in animals.keys():
    print(f'{animal} -> {animals[animal][0]}g')
print('Areas with hungry animals:')
for area, hungry_animals in areas.items():
    if hungry_animals != 0:
        print(f'{area}: {hungry_animals}')