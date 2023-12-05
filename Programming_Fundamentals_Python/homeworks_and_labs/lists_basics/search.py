n = int(input())
keyword = input()

search_list = []

for _ in range(n):
    current_string = input()
    search_list.append(current_string)
print(search_list)

sorted_strings_list = []

for element in search_list:
    if keyword in element:
        sorted_strings_list.append(element)
print(sorted_strings_list)

# SECOND OPTION

# n = int(input())
# keyword = input()
#
# search_list = []
#
# for _ in range(n):
#     current_string = input()
#     search_list.append(current_string)
# print(search_list)
#
# for element in search_list[::-1]:
#     if keyword not in element:
#         search_list.remove(element)
# print(search_list)