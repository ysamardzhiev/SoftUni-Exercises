text = input()

emoticons = []
for i in range(len(text)):
    if text[i] == ':':
        emoticons.append(text[i+1])

for emoji in emoticons:
    print(f':{emoji}')