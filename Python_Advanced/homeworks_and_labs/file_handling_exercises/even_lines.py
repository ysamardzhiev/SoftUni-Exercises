import os

path = os.path.join('files', 'text.txt')

with open(path, 'r') as file:
    lines = file.readlines()

swappable_symbols = ["-", ",", ".", "!", "?"]

for i in range(0, len(lines), 2):
    line = lines[i].strip()

    for char in swappable_symbols:
        if char in line:
            line = line.replace(char, '@')

    print(' '.join(line.split()[::-1]))