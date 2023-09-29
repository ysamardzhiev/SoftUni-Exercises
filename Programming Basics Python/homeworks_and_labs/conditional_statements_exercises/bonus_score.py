starter_points = int(input())
bonus_points = 0

if starter_points <= 100:
    bonus_points = 5
elif starter_points < 1000:
    bonus_points = starter_points * 0.2
else:
    bonus_points = starter_points * 0.1


if starter_points % 2 == 0:
    bonus_points = bonus_points + 1
elif starter_points % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(starter_points + bonus_points)