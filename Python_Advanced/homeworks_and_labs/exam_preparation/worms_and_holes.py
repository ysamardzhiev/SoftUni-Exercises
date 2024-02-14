from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

total_worms = len(worms)
matches = 0

while holes and worms:
    cur_worm = worms.pop()
    cur_hole = holes.popleft()

    if cur_worm == cur_hole:
        matches += 1
        continue

    if cur_worm - 3 > 0:
        worms.append(cur_worm - 3)

print(f"Matches: {matches}") if matches else print("There are no matches.")

if total_worms == matches:
    print("Every worm found a suitable hole!")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
else:
    print("Worms left: none")

if holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
else:
    print("Holes left: none")