def odd_even_sum(number: str) -> str:
    even_sum = 0
    odd_sum = 0
    for digit in number:
        digit_as_int = int(digit)
        if digit_as_int % 2 == 0:
            even_sum += digit_as_int
        else:
            odd_sum += digit_as_int
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_as_str = input()
result = odd_even_sum(number_as_str)
print(result)