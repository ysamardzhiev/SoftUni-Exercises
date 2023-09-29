# How much will I have if i get 1$ every second in a day

dollars_a_day = 0

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            dollars_a_day += 1

print(f'{dollars_a_day:.2f}')
