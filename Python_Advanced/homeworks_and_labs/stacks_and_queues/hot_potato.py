from collections import deque

players = deque(input().split())
n_toss = int(input())

current_toss = 0

while len(players) != 1:
    for player in players:
        current_toss += 1
        if current_toss == n_toss:
            print(f'Removed {player}')
            players.remove(player)
            current_toss = 0
        else:
            players.remove(player)
            players.append(player)
        break
print(f'Last is {players.pop()}')