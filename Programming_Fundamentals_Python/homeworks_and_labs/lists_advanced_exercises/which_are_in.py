first_string = input().split(', ')
second_string = input().split(', ')

valid_substrings = []
for substring in first_string:
    for string in second_string:
        if substring in string:
            valid_substrings.append(substring)
            break
print(valid_substrings)