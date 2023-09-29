starting_hours = int(input())
starting_minutes = int(input())

total_time_in_min = (starting_hours * 60) + starting_minutes + 15
hours = total_time_in_min // 60
minutes = total_time_in_min % 60

if hours > 23:
    hours = 0

print(f'{hours}:{minutes:02}')

