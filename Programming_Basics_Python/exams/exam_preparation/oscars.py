name_of_actor = input()
academy_points = float(input())
jury_count = int(input())

total_points = 0

for i in range(jury_count):
    name_of_jury = input()
    given_points = float(input())

    name_length = int(len(name_of_jury))
    if i == 0:
        total_points = academy_points + (name_length * given_points) / 2
    elif total_points > 1250.5:
        break
    else:
        total_points = total_points + (name_length * given_points) / 2

if total_points >= 1250.5:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = abs(total_points - 1250.5)
    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')