sent_off_players = input().split()

team_A_players = []
team_B_players = []
game_terminated = False

for player_num in range(1, 12):
    team_A_players.append(f'A-{player_num}')
for player_num in range(1, 12):
    team_B_players.append(f'B-{player_num}')

for player in sent_off_players:
    if player in team_A_players:
        team_A_players.remove(player)
    elif player in team_B_players:
        team_B_players.remove(player)
    if len(team_A_players) < 7 or len(team_B_players) < 7:
        game_terminated = True
        break
print(f"Team A - {len(team_A_players)}; Team B - {len(team_B_players)}")
if game_terminated:
    print('Game was terminated')