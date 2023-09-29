first_interval = input()
second_interval = input()

for num_1 in range(int(first_interval[0]), int(second_interval[0]) + 1):
    for num_2 in range(int(first_interval[1]), int(second_interval[1]) + 1):
        for num_3 in range(int(first_interval[2]), int(second_interval[2]) + 1):
            for num_4 in range(int(first_interval[3]), int(second_interval[3]) + 1):
                if num_1 % 2 and num_2 % 2 and num_3 % 2 and num_4 % 2:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=" ")
