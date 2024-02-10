def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*tuples):
    result = ''

    for func, args in tuples:
        func_name = func.__name__
        func_result = func(*args)
        result += f'{func_name} - {func_result}' + '\n'

    return result


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
