n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(letter) for letter in name) // row

    if ascii_sum % 2:
        odd_set.add(ascii_sum)
    else:
        even_set.add(ascii_sum)

odd_numbers_sum = sum(odd_set)
even_numbers_sum = sum(even_set)

if odd_numbers_sum == even_numbers_sum:
    print(*odd_set.union(even_set), sep=', ')
elif even_numbers_sum > odd_numbers_sum:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
else:
    print(*odd_set.difference(even_set), sep=', ')