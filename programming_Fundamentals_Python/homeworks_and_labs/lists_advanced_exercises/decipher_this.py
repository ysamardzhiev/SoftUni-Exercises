def swap_characters(some_letters: list) -> str:
    some_letters[0], some_letters[-1] = some_letters[-1], some_letters[0]
    return ''.join(some_letters)


secret_message = input().split()

message_reveal = []
for word in secret_message:
    ascii_number = ''
    letters = []
    for char in word:
        if char.isdigit():
            ascii_number += char
        else:
            letters += char
    final_word = chr(int(ascii_number)) + swap_characters(letters)
    message_reveal.append(final_word)
print(' '.join(message_reveal))