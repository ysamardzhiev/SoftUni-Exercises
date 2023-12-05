text = input()

final_text = ''
for i in range(len(text)):
    if i == 0:
        final_text += text[i]
    elif text[i] != text[i-1]:
        final_text += text[i]
print(final_text)