first_char = int(input())
last_char = int(input())

for current_char in range(first_char, last_char + 1):
    print(chr(current_char), end=' ')