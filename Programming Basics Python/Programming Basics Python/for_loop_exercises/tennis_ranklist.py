from math import floor
tournament_count = int(input())
starting_points = int(input())

new_points = 0
total_won_tournaments = 0
total_final_tournaments = 0
total_semi_final_tournaments = 0

for _ in range(tournament_count):
    tournament_placement = input()
    if tournament_placement == 'W':
        new_points += 2000
        total_won_tournaments += 1
    elif tournament_placement == 'F':
        new_points += 1200
        total_final_tournaments += 1
    elif tournament_placement == 'SF':
        new_points += 720
        total_semi_final_tournaments += 1

total_points = starting_points + new_points
average_points = ((total_won_tournaments * 2000) + (total_final_tournaments * 1200) +
                  (total_semi_final_tournaments * 720)) / tournament_count
winning_percent = (total_won_tournaments / tournament_count) * 100
print(f'Final points: {floor(total_points)}')
print(f'Average points: {floor(average_points)}')
print(f'{winning_percent:.2f}%')