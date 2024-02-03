matrix = [el.split() for el in input().split('|')]
flatten_list = [el for row in matrix[::-1] for el in row]

print(' '.join(flatten_list))