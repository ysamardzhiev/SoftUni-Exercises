def positive_numbers(some_numbers: list) -> str:
    positive = [str(number) for number in some_numbers if number >= 0]
    return ', '.join(positive)


def negative_numbers(some_numbers: list) -> str:
    negative = [str(number) for number in some_numbers if number < 0]
    return ', '.join(negative)


def even_numbers(some_numbers: list) -> str:
    even = [str(number) for number in some_numbers if number % 2 == 0]
    return ', '.join(even)


def odd_numbers(some_numbers: list) -> str:
    odd = [str(number) for number in some_numbers if number % 2]
    return ', '.join(odd)


numbers = [int(number) for number in input().split(', ')]

print(f'Positive: {positive_numbers(numbers)}')
print(f'Negative: {negative_numbers(numbers)}')
print(f'Even: {even_numbers(numbers)}')
print(f'Odd: {odd_numbers(numbers)}')
