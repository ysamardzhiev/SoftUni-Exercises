text = input()

digits = ''
letters = ''
special_characters = ''

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        special_characters += char
print(digits)
print(letters)
print(special_characters)