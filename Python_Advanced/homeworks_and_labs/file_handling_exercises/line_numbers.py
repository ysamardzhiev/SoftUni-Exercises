import os

text_path = os.path.join('files', 'text.txt')
output_path = os.path.join('files', 'output.txt')

with open(text_path, 'r') as file:
    text = file.readlines()

with open(output_path, 'w') as file:
    current_row = 0
    for line in text:
        letters, punc_marks = 0, 0
        current_row += 1
        for char in line.strip():
            if char.isspace():
                continue
            elif char.isalpha():
                letters += 1
            else:
                punc_marks += 1
        file.write(f"Line {current_row}: {line.strip()} ({letters})({punc_marks})\n")
