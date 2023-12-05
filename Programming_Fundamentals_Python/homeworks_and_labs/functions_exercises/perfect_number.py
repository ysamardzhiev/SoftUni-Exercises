def perfect_number(some_number: int) -> str:
    positive_divisors_sum = 0
    for current_number in range(1, some_number):
        if some_number % current_number == 0:
            positive_divisors_sum += current_number

    if positive_divisors_sum == some_number:
        return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))