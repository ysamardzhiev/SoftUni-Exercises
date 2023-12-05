text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
text_without_vowels = [letter for letter in text if letter.lower() not in vowels]
print(''.join(text_without_vowels))