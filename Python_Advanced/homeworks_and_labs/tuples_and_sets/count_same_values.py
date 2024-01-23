numbers = tuple(input().split())
used_numbers = []

for number in numbers:
    if number not in used_numbers:
        print(f'{float(number)} - {numbers.count(number)} times')
        used_numbers.append(number)