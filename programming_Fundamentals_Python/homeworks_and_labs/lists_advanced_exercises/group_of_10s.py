from math import ceil

numbers = [int(number) for number in input().split(', ')]

max_number = ceil(max(numbers) / 10)
for group in range(1, max_number + 1):
    groups_of_numbers = []
    group_of_10s = group * 10
    for current_number in numbers:
        if group_of_10s - 10 < current_number <= group_of_10s:
            groups_of_numbers.append(current_number)
    print(f"Group of {group_of_10s}'s: {groups_of_numbers}")