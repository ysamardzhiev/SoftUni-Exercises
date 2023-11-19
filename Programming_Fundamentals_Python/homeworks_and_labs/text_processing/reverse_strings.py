command = input()
while command != 'end':
    word = command
    reversed_word = [word[index] for index in range(len(word) - 1, -1, -1)]
    print(f"{word} = {''.join(reversed_word)}")
    command = input()