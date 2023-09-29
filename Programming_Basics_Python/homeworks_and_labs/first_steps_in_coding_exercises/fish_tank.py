lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_fish_tank = lenght * width * height
volume_lt = volume_fish_tank / 1000
occupied_space = percent
needed_lt = volume_lt * (1 - percent / 100)

print(needed_lt)