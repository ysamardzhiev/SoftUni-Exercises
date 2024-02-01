n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n)]

diagonals_difference = abs(sum(primary) - sum(secondary))
print(diagonals_difference)