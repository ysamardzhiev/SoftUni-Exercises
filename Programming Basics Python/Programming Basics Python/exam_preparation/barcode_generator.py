first_interval = input()
second_interval = input()

for num1 in range(int(first_interval[0]), int(second_interval[0]) + 1):
    for num2 in range(int(first_interval[1]), int(second_interval[1]) + 1):
        for num3 in range(int(first_interval[2]), int(second_interval[2]) + 1):
            for num4 in range(int(first_interval[3]), int(second_interval[3]) + 1):
                if num1 % 2 and num2 % 2 and num3 % 2 and num4 % 2:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
