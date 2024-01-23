n = int(input())
names = [input() for _ in range(n)]
print('\n'.join(set(names)))