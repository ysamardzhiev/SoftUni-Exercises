element = input()

characters = {}

for char in element:
    if char == ' ':
        continue

    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

for current_char in characters.keys():
    print(f'{current_char} -> {characters[current_char]}')