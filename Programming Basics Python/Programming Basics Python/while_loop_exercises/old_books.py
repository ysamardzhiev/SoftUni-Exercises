wanted_book = input()

books_counter = 0

while True:
    current_book = input()
    if current_book == wanted_book:
        print(f'You checked {books_counter} books and found it.')
        break
    elif current_book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {books_counter} books.')
        break
    books_counter += 1
