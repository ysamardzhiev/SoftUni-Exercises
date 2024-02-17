def team_lineup(*players):
    players_info = {}

    for player, country in players:
        if country not in players_info:
            players_info[country] = []
        players_info[country].append(player)

    sorted_players = sorted(players_info.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''

    for country, players_info in sorted_players:
        result += f'{country}:\n'
        for player in players_info:
            result += f'  -{player}\n'

    return result


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
