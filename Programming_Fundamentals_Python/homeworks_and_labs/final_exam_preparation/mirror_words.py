import re

text = input()

matches = re.findall(r"(@|#)([a-zA-Z]{3,})\1", text)

if matches:
    print(f"{len(matches)} word pairs found!")
    print('The mirror words are:')
    print(matches)