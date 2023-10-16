list_of_numbers_as_str = input().split()
n = int(input())

list_of_numbers_as_int = []

for number in list_of_numbers_as_str:
    list_of_numbers_as_int.append(int(number))

for _ in range(n):
    smallest_number = min(list_of_numbers_as_int)
    list_of_numbers_as_int.remove(smallest_number)

list_of_numbers_as_str.clear()
for current_num in list_of_numbers_as_int:
    list_of_numbers_as_str.append(str(current_num))
print(', '.join(list_of_numbers_as_str))