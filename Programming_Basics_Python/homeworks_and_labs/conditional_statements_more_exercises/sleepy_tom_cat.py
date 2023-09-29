rest_days_count = int(input())

rest_days_total = rest_days_count * 127
work_days_total = (365 - rest_days_count) * 63
playtime = rest_days_total + work_days_total
diff = abs(playtime - 30000)
hours = diff // 60
minutes = diff % 60

if playtime > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')