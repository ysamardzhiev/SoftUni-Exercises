input_line = input()

the_most_powerful_word = ''
the_most_powerful_word_sum = 0

while input_line != 'End of words':
    current_word = input_line
    total_symbols_sum = 0
    for letter in current_word:
        total_symbols_sum += ord(letter)

    if current_word[0].lower() in 'aeiouy':
        total_symbols_sum *= len(current_word)
    else:
        total_symbols_sum //= len(current_word)

    if total_symbols_sum > the_most_powerful_word_sum:
        the_most_powerful_word_sum = total_symbols_sum
        the_most_powerful_word = current_word

    input_line = input()

print(f'The most powerful word is {the_most_powerful_word} - {the_most_powerful_word_sum}')