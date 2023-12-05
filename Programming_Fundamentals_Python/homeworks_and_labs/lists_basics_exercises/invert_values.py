numbers_list = input().split()

opposite_numbers = []

for element in numbers_list:
    number_in_int = -int(element)
    opposite_numbers.append(number_in_int)
print(opposite_numbers)
