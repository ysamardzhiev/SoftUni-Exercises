month = input()
hours_count = int(input())
people_count = int(input())
time_of_the_day = input()

price_for_entry = 0

if month == 'march' or month == 'april' or month == 'may':
    if time_of_the_day == 'day':
        price_for_entry = 10.50
    elif time_of_the_day == 'night':
        price_for_entry = 8.40
elif month == 'june' or month == 'july' or month == 'august':
    if time_of_the_day == 'day':
        price_for_entry = 12.60
    elif time_of_the_day == 'night':
        price_for_entry = 10.20

if people_count >= 4:
    price_for_entry = price_for_entry * 0.90

if hours_count >= 5:
    price_for_entry = price_for_entry * 0.50

total_cost = (price_for_entry * people_count) * hours_count

print(f'Price per person for one hour: {price_for_entry:.2f}\nTotal cost of the visit: {total_cost:.2f}')