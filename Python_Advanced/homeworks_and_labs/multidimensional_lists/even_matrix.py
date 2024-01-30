rows = int(input())

even_matrix = [[int(num) for num in input().split(', ') if int(num) % 2 == 0] for row in range(rows)]
print(even_matrix)