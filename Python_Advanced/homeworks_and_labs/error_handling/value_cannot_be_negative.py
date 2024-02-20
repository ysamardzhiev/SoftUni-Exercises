class ValueCannotBeNegative(Exception):
    """Raises exception when the number is negative"""
    pass


for _ in range(5):
    try:
        number = int(input())
    except ValueError:
        print('Invalid input')
        break

    if number < 0:
        raise ValueCannotBeNegative
