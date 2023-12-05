import re

text = input()
word = input()

occurrences = re.findall(fr"\b{word}\b", text, re.IGNORECASE)
print(len(occurrences))