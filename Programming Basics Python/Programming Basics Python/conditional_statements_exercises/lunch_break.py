from math import ceil
name = str(input())
episode_duration = int(input())
rest_duration = int(input())

time_for_lunch = rest_duration * 1/8
time_for_rest = rest_duration * 1/4
leftover_time = rest_duration - time_for_lunch - time_for_rest
diff = abs(leftover_time - episode_duration)

if leftover_time >= episode_duration:
    print(f"You have enough time to watch {name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(diff)} more minutes.")