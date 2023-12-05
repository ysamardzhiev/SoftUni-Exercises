import re

text = input()
while text:
    match = re.findall(r"www\.[a-zA-Z0-9\]-]+\.[a-z\\.]+", text)
    if match:
        print(''.join(match))
    text = input()