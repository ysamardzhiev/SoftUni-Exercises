characters = input().split(', ')

ascii_chars = {char: ord(char) for char in characters}
print(ascii_chars)