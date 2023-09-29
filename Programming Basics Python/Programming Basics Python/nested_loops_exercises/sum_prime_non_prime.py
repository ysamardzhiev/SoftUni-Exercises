input_line = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0
counter = 0

while input_line != 'stop':
    current_number = int(input_line)
    if current_number < 0:
        print('Number is negative.')
        input_line = input()
        continue
    for i in range(1, current_number + 1):
        if current_number % i == 0:
            counter += 1
    if counter > 2:
        non_prime_numbers_sum += current_number
    else:
        prime_numbers_sum += current_number
    counter = 0
    input_line = input()
print(f'Sum of all prime numbers is: {prime_numbers_sum}\nSum of all non prime numbers is: {non_prime_numbers_sum}')