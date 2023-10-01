number = int(input())

for current_num in range(1, number + 1):
    current_num = str(current_num)
    digits_sum = 0
    special_number = False

    for digit in current_num:
        digits_sum += int(digit)
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        special_number = True

    print(f"{current_num} -> {special_number}")