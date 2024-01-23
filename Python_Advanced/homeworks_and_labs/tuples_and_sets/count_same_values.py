numbers = (input().split(),)
used_numbers = []

for number in numbers[0]:
    if number not in used_numbers:
        print(f'{float(number)} - {numbers[0].count(number)} times')
        used_numbers.append(number)