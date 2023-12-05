number_of_chars = int(input())

total_ascii_sum = 0

for letter in range(number_of_chars):
    current_ascii_char = input()
    total_ascii_sum += ord(current_ascii_char)

print(f"The sum equals: {total_ascii_sum}")