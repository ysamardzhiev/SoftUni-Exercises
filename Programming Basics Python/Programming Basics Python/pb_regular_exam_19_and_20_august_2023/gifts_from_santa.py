N = int(input())
M = int(input())
S = int(input())

for num in reversed(range(N, M + 1)):
    if num % 2 == 0 and num % 3 == 0:
        if num == S:
            break
        else:
            print(num, end=' ')