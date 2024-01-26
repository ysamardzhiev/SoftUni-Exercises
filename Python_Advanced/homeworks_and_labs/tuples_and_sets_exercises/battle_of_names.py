n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)

    final_result = ascii_sum // row

    if final_result % 2:
        odd_set.add(final_result)
    else:
        even_set.add(final_result)

odd_numbers_sum = sum(odd_set)
even_numbers_sum = sum(even_set)

if odd_numbers_sum == even_numbers_sum:
    print(*odd_set.union(even_set), sep=', ')
elif even_numbers_sum > odd_numbers_sum:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
else:
    print(*odd_set.difference(even_set), sep=', ')