number_sold_games = int(input())

hs_counter = 0
fortnite_counter = 0
ow_counter = 0
others_counter = 0

for _ in range(number_sold_games):
    game_name = input()
    if game_name == 'Hearthstone':
        hs_counter += 1
    elif game_name == 'Fornite':
        fortnite_counter += 1
    elif game_name == 'Overwatch':
        ow_counter += 1
    else:
        others_counter += 1

hs_percent = hs_counter / number_sold_games * 100
fortnite_percent = fortnite_counter / number_sold_games * 100
ow_percent = ow_counter / number_sold_games * 100
others_percent = others_counter / number_sold_games * 100

print(f'Hearthstone - {hs_percent:.2f}%')
print(f'Fornite - {fortnite_percent:.2f}%')
print(f'Overwatch - {ow_percent:.2f}%')
print(f'Others - {others_percent:.2f}%')