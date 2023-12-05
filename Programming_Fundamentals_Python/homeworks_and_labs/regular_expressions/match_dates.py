import re

dates = input()
pattern = r"\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(pattern, dates)

for date in matches:
    day, month, year = date[0], date[2], date[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')