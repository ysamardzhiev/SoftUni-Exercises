n = int(input())

current_num = 1
flag = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(current_num, end=' ')
        current_num += 1
        if current_num > n:
            flag = True
            break
    if flag:
        break
    print()