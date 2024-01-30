rows = int(input())

flattened_matrix = [int(num) for row in range(rows) for num in input().split(', ')]
print(flattened_matrix)