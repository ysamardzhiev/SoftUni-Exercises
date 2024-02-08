from functools import reduce


def operate(operator, *args):
    operations = {
        '+': reduce(lambda x, y: x + y, args),
        '-': reduce(lambda x, y: x - y, args),
        '*': reduce(lambda x, y: x * y, args),
        '/': reduce(lambda x, y: x / y, args)
    }

    return operations[operator]


print(operate("+", 1, 2, 3))
print(operate("/", 32, 2))