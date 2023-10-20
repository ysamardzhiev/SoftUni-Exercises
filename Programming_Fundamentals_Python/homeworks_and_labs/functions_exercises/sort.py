numbers_as_string = input().split()

numbers_as_int = []
for number in numbers_as_string:
    numbers_as_int.append(int(number))

print(sorted(numbers_as_int))