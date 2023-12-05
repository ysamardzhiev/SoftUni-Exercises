number = [int(digit) for digit in input()]

largest_number = sorted(number, reverse=True)
largest_number = [str(digit) for digit in largest_number]
print(''.join(largest_number))