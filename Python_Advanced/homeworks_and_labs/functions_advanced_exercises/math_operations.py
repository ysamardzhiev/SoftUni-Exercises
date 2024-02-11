from collections import deque


def math_operations(*floats, **kwargs):
    numbers = deque(floats)

    while numbers:
        for letter in kwargs:
            if not numbers:
                break
            current_num = numbers.popleft()
            if letter == 'a':
                kwargs[letter] += current_num
            elif letter == 's':
                kwargs[letter] -= current_num
            elif letter == 'd':
                if current_num != 0 and kwargs[letter] != 0:
                    kwargs[letter] /= current_num
            elif letter == 'm':
                kwargs[letter] *= current_num

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{k}: {v:.1f}" for k, v in result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))