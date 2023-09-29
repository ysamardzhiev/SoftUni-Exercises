days_counter = 0
pages_counter = 0
total_pages = 400

for days in range(365):
    days_counter += 1
    pages_counter += 15
    if pages_counter >= total_pages:
        break


print(days_counter)