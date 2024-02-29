import os

text_path = os.path.join('files', 'text.txt')
output_path = os.path.join('files', 'output.txt')

with open(text_path, 'r') as file:
    text = file.readlines()

with open(output_path, 'w') as file:
    for row in range(len(text)):
        letters, punc_marks = 0, 0
        line = text[row].strip()
        for char in line:
            if char.isspace():
                continue
            elif char.isalpha():
                letters += 1
            else:
                punc_marks += 1
        file.write(f"Line {row + 1}: {line} ({letters})({punc_marks})\n")
