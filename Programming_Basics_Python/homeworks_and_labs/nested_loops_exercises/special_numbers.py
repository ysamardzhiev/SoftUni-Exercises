n = int(input())

for i in range(1111, 10000):
    current_number_in_str = str(i)
    counter = 0
    for digits in range(len(current_number_in_str)):
        digit = int(current_number_in_str[digits])
        if digit == 0:
            continue
        elif n % digit == 0:
            counter += 1

        if counter == 4:
            print(current_number_in_str, end=' ')