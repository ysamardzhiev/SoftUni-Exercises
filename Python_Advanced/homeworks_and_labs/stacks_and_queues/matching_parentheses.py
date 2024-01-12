expression = input()

opening_parenthesis = []

for index in range(len(expression)):
    if expression[index] == '(':
        opening_parenthesis.append(index)
    elif expression[index] == ')':
        start_index = opening_parenthesis.pop()
        print(expression[start_index:index+1])