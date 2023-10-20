def is_palindrome_number(number: str) -> bool:
    return number[::-1] == number


numbers_as_str = input().split(', ')
for current_number in numbers_as_str:
    print(is_palindrome_number(current_number))


# SECOND OPTION
#
# def is_palindrome_number(numbers: list):
#     for current_number in numbers:
#         backwards_number = ''
#         for index in range(len(current_number) - 1, -1, -1):
#             backwards_number += current_number[index]
#         if current_number == backwards_number:
#             print('True')
#         else:
#             print('False')
#
#
# numbers_as_str = input().split(', ')
# is_palindrome_number(numbers_as_str)