def round_numbers(numbers_as_string):
    rounded_list = []
    for number in numbers_as_string:
        rounded_list.append(round(float(number)))
    return rounded_list


numbers_as_string = input().split()
print(round_numbers(numbers_as_string))