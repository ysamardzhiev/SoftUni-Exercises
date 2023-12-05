numbers = [int(digit) for digit in input().split(', ')]

for number in numbers:
    if number == 0:
        numbers.append(number)
        numbers.remove(number)
print(numbers)