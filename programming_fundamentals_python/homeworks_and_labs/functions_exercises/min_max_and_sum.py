def int_convert(numbers: list) -> list:
    numbers_as_int = []
    for number in numbers:
        numbers_as_int.append(int(number))
    return numbers_as_int


numbers_as_string = input().split()
final_list = int_convert(numbers_as_string)
print(f"The minimum number is {min(final_list)}\n"
      f"The maximum number is {max(final_list)}\n"
      f"The sum number is: {sum(final_list)}")