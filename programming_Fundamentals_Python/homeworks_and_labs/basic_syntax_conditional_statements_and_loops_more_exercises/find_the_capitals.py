string = input()

capital_letters_indices = [index for index in range(len(string)) if string[index].isupper()]
print(capital_letters_indices)