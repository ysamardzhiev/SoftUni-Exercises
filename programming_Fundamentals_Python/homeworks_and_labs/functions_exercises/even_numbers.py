numbers_as_str = input().split()

numbers_as_int = []

for number in numbers_as_str:
    numbers_as_int.append(int(number))

filtered_numbers = filter(lambda num: num % 2 == 0, numbers_as_int)
print(list(filtered_numbers))