year = int(input())

is_happy_year = False

while True:
    year += 1

    for digit in str(year):
        if str(year).count(digit) > 1:
            break
    else:
        is_happy_year = True

    if is_happy_year:
        print(year)
        break

# number = int(input())
#
# is_happy_year = False
#
# while True:
#     number += 1
#     digits_list = []
#
#     for digit in str(number):
#         if digit in digits_list:
#             break
#         digits_list.append(digit)
#     else:
#         is_happy_year = True
#
#     if is_happy_year:
#         print(number)
#         break
