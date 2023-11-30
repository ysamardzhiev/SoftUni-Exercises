import re

some_string = input()

while some_string:
    matched_numbers = re.findall(r"\d+", some_string)
    if matched_numbers:
        print(' '.join(matched_numbers), end=' ')
    some_string = input()