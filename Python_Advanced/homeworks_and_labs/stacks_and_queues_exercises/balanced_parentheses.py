from collections import deque

opening_parentheses = deque()

for parentheses in input():
    if parentheses in ['(', '{', '[']:
        opening_parentheses.append(parentheses)
    else:
        if not opening_parentheses:
            print('NO')
            break
        open_par = opening_parentheses.pop()
        if open_par == '(' and parentheses == ')':
            continue
        elif open_par == '{' and parentheses == '}':
            continue
        elif open_par == '[' and parentheses == ']':
            continue
        else:
            print('NO')
            break
else:
    print('YES')