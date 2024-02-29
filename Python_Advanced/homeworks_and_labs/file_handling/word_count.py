import re
import os

words_path = os.path.join('files', 'words.txt')
text_path = os.path.join('files', 'input.txt')
output_path = os.path.join('files', 'output.txt')

with open(words_path) as file:
    searched_words = [word.lower() for word in file.read().split()]

with open(text_path) as file:
    text = file.read().lower()

matching_words = {}

for searched_word in searched_words:
    matches = re.findall(rf"\b{searched_word}\b", text)
    matching_words[searched_word] = len(matches)

with open(output_path, 'w') as file:
    sorted_words = sorted(matching_words.items(), key=lambda x: -x[1])
    for word, count in sorted_words:
        file.write(f'{word} - {count}\n')