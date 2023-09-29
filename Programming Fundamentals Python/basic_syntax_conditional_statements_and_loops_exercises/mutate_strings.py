first_string = input()
second_string = input()

for char in range(len(first_string)):

    left_side = second_string[:char + 1]
    right_side = first_string[char + 1:]

    if first_string[char] == second_string[char]:
        continue

    print(f"{left_side}{right_side}")