import os

path = os.path.join('text.txt')

try:
    file = open(path)
    print('File found')
except FileNotFoundError:
    print('File not found')
