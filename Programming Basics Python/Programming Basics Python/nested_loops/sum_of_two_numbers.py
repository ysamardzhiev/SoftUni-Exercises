first_number = int(input())
second_number = int(input())
n = int(input())

counter = 0
flag = False

for n1 in range(first_number, second_number + 1):
    for n2 in range(first_number, second_number + 1):
        counter += 1
        if n1 + n2 == n:
            print(f"Combination N:{counter} ({n1} + {n2} = {n})")
            flag = True
            break
    if flag:
        break
else:
    print(f"{counter} combinations - neither equals {n}")