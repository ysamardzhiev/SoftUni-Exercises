number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

total_time_of_reading = number_of_pages // pages_per_hour

necessary_hours_per_day = total_time_of_reading // number_of_days

print(necessary_hours_per_day)