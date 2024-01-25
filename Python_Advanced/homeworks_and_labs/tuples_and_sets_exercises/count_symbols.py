text = input()

characters = {}

for char in text:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1

for char in sorted(characters):
    print(f'{char}: {characters[char]} time/s')