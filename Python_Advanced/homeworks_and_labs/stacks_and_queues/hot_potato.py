from collections import deque

players = deque(input().split())
n_toss = int(input()) - 1

while len(players) != 1:
    players.rotate(-n_toss)
    removed_player = players.popleft()
    print(f'Removed {removed_player}')
last_player = players.popleft()
print(f'Last is {last_player}')