import re

dates = input()
pattern = r"\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(pattern, dates)

for date in matches:
    print(f'Day: {date[0]}, Month: {date[2]}, Year: {date[3]}')