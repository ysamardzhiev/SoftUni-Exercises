characters_count = int(input())

for i in range(characters_count):
    for k in range(characters_count):
        for j in range(characters_count):
            print(f'{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}')