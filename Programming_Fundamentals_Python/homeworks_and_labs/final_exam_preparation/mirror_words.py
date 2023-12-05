import re


def check_validity(text):
    valid_pairs = []
    matches = re.finditer(r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1", text)
    for word in matches:
        valid_pairs.append((word.group(2), word.group(3)))
    return valid_pairs


text = input()

mirror_words = []

if check_validity(text):
    print(f"{len(check_validity(text))} word pairs found!")
    for word1, word2 in check_validity(text):
        if word1 == word2[::-1]:
            mirror_words.append(f'{word1} <=> {word2}')
else:
    print("No word pairs found!")

if mirror_words:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print('No mirror words!')
