animals = input().split(', ')
animals_reversed = [animals[animal_index] for animal_index in range(len(animals) - 1, -1, -1)]

for index in range(1, len(animals_reversed) + 1):
    if animals_reversed[0] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    elif animals_reversed[index - 1] == 'wolf':
        print(f'Oi! Sheep number {index - 1}! You are about to be eaten by a wolf!')
        break