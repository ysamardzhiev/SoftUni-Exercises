total_steps = 0
going_home_counter = 0

while total_steps < 10000:
    steps = input()
    if going_home_counter == 1:
        steps = int(steps)
        total_steps += steps
        break
    elif steps == 'Going home':
        going_home_counter += 1
        continue
    steps = int(steps)
    total_steps += steps

diff = abs(total_steps - 10000)
if going_home_counter == 1:
    if total_steps >= 10000:
        print('Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
    else:
        print(f'{diff} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')