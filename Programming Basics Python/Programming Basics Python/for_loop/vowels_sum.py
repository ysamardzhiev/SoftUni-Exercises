letter = input()

value = 0

for i in range(len(letter)):
    if letter[i] == 'a':
        value = 1 + value
    if letter[i] == 'e':
        value = 2 + value
    if letter[i] == 'i':
        value = 3 + value
    if letter[i] == 'o':
        value = 4 + value
    if letter[i] == 'u':
        value = 5 + value

print(value)