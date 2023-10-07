number_of_snowballs = int(input())

highest_value = 0
highest_weight = 0
highest_time = 0
highest_quality = 0

for current_snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    overall_value = (weight / time) ** quality

    if overall_value > highest_value:
        highest_value = overall_value
        highest_weight = weight
        highest_time = time
        highest_quality = quality
print(f"{highest_weight} : {highest_time} = {int(highest_value)} ({highest_quality})")