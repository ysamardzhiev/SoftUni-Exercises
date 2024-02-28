import re


with open('words.txt') as file:
    searched_words = [word.lower() for word in file.read().split()]

with open('input.txt') as file:
    text = file.read().lower()

matching_words = {}

for searched_word in searched_words:
    matches = re.findall(rf"\b{searched_word}\b", text)
    matching_words[searched_word] = len(matches)

with open('output.txt', 'w') as file:
    sorted_words = sorted(matching_words.items(), key=lambda x: -x[1])
    for word, count in sorted_words:
        file.write(f'{word} - {count}\n')