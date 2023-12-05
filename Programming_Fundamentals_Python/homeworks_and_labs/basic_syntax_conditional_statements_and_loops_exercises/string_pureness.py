# number_of_strings = int(input())
#
# for _ in range(number_of_strings):
#     current_string = input()
#     if ',' in current_string or '.' in current_string or '_' in current_string:
#         print(f"{current_string} is not pure!")
#     else:
#         print(f"{current_string} is pure.")

number_of_strings = int(input())

for _ in range(number_of_strings):
    current_string = input()
    not_pure = False
    for char in current_string:
        if char == ',' or char == '.' or char == '_':
            not_pure = True
            break
    if not_pure:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")