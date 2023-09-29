input_change = float(input())
total_change = int(input_change * 100)
counter = 0

while total_change > 0:
    if total_change >= 200:
        total_change -= 200
    elif total_change >= 100:
        total_change -= 100
    elif total_change >= 50:
        total_change -= 50
    elif total_change >= 20:
        total_change -= 20
    elif total_change >= 10:
        total_change -= 10
    elif total_change >= 5:
        total_change -= 5
    elif total_change >= 2:
        total_change -= 2
    elif total_change >= 1:
        total_change -= 1

    counter += 1

print(counter)