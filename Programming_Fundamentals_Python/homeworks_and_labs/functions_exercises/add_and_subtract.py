def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(add_result: int, num3: int) -> int:
    return add_result - num3


def add_and_subtract(num1: int, num2: int, num3: int) -> int:
    returned_result = sum_numbers(num1, num2)
    final_result = subtract(returned_result, num3)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)