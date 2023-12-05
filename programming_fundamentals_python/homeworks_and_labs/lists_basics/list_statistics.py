n = int(input())

negative_numbers = []
positive_numbers = []
negative_numbers_sum = 0

for _ in range(n):
    current_number = int(input())
    if current_number < 0:
        negative_numbers.append(current_number)
        negative_numbers_sum += current_number
    else:
        positive_numbers.append(current_number)
print(f"{positive_numbers}\n"
      f"{negative_numbers}\n"
      f"Count of positives: {len(positive_numbers)}\n"
      f"Sum of negatives: {negative_numbers_sum}")