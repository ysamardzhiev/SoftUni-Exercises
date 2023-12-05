strings = input().split()

even_strings = [string for string in strings if len(string) % 2 == 0]
print('\n'.join(even_strings))