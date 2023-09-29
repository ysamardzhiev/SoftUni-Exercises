groups_count = int(input())
total_climbers = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0


for _ in range(groups_count):
    current_number_of_group = int(input())
    total_climbers += current_number_of_group

    if current_number_of_group <= 5:
        musala += current_number_of_group
    elif 6 <= current_number_of_group <= 12:
        monblan += current_number_of_group
    elif 13 <= current_number_of_group <= 25:
        kilimanjaro += current_number_of_group
    elif 26 <= current_number_of_group <= 40:
        k2 += current_number_of_group
    elif current_number_of_group >= 41:
        everest += current_number_of_group

total_climbers_musala = musala / total_climbers * 100
total_climbers_monblan = monblan / total_climbers * 100
total_climbers_kilimanjaro = kilimanjaro / total_climbers * 100
total_climbers_k2 = k2 / total_climbers * 100
total_climbers_everest = everest / total_climbers * 100

print(f'{total_climbers_musala:.2f}%')
print(f'{total_climbers_monblan:.2f}%')
print(f'{total_climbers_kilimanjaro:.2f}%')
print(f'{total_climbers_k2:.2f}%')
print(f'{total_climbers_everest:.2f}%')