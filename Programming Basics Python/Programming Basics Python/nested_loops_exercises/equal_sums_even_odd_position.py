first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    current_number_in_str = str(i)

    even_sum = 0
    odd_sum = 0
    for digits in range(len(current_number_in_str)):
        current_digit = int(current_number_in_str[digits])

        if digits % 2:
            odd_sum += current_digit
        else:
            even_sum += current_digit

    if even_sum == odd_sum:
        print(current_number_in_str, end=' ')
