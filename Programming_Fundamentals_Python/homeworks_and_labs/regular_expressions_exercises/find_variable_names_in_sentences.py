import re

text = input()

matches = re.findall(r"\b_([a-zA-Z0-9]+)\b", text)
print(','.join(matches))