numbers = input().split()

abs_list = []

for number in numbers:
    abs_list.append(abs(float(number)))
print(abs_list)