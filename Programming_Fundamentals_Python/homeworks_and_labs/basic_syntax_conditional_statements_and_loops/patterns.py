number = int(input())

# Main body

for i in range(1, number + 1):
    for j in range(i):
        print('*', end='')
    print()

# Mirror body

for i in range(number - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()