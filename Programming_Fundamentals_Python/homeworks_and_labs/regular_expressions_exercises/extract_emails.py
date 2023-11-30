import re

text = input()

valid_emails = re.finditer(r"\s(([a-z0-9]+[a-z0-9\\.\-\\_]*)@([a-z\-]+)(\.[a-z\-]+)+)\b", text)

for email in valid_emails:
    print(email.group())
