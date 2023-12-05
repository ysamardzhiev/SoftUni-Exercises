n = int(input())

saved_brackets = []
balanced = True
for _ in range(n):
    element = input()
    if element == '(' or element == ')':
        saved_brackets.append(element)

for index in range(len(saved_brackets) - 1):
    if saved_brackets[0] == ')':
        balanced = False
    if saved_brackets[index] == '(' and saved_brackets[index + 1] == '(':
        balanced = False
    elif saved_brackets[index] == ')' and saved_brackets[index + 1] == ')':
        balanced = False
    if not balanced:
        print('UNBALANCED')
        break
else:
    print('BALANCED')