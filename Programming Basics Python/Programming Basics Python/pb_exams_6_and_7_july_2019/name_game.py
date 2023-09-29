input_line = input()

highest_points_name = ''
highest_points = 0

while input_line != 'Stop':
    name = input_line
    total_points = 0
    for letter in name:
        current_number = int(input())
        if current_number == ord(letter):
            total_points += 10
        else:
            total_points += 2

    if total_points >= highest_points:
        highest_points = total_points
        highest_points_name = name

    input_line = input()

print(f'The winner is {highest_points_name} with {highest_points} points!')