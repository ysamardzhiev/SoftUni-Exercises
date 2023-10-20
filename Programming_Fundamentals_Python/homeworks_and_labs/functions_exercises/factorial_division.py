def calculate_factorial(number: int) -> int:
    total_value = 1
    for factorial in range(number, 0, -1):
        total_value *= factorial
    return total_value


first_number = int(input())
second_number = int(input())
final_result = calculate_factorial(first_number) / calculate_factorial(second_number)
print(f'{final_result:.2f}')

# SECOND OPTION
#
# from math import factorial
#
#
# def factorial_division(num1: int, num2: int) -> float:
#     result = factorial(num1) / factorial(num2)
#     return result
#
#
# first_number = int(input())
# second_number = int(input())
# final_result = factorial_division(first_number, second_number)
# print(f'{final_result:.2f}')

