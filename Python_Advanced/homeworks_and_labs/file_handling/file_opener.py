import os

path = os.path.join('files', 'text.txt')

try:
    file = open(path)
    print('File found')
except FileNotFoundError:
    print('File not found')
