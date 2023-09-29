actor = input()
academy_points = float(input())
judges_count = int(input())

given_points = 0
name_length = 0

for i in range(judges_count):
    judge_name = input()
    points_from_judge = float(input())

    name_length = len(judge_name)
    if i > 0:
        academy_points = 0
    given_points = given_points + academy_points + ((name_length * points_from_judge) / 2)
    if given_points >= 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {given_points:.1f}!")
        break
else:
    diff = abs(1250.5 - given_points)
    print(f"Sorry, {actor} you need {diff:.1f} more!")