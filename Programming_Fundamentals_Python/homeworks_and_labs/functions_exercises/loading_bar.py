def loading_bar(some_number: int) -> str:
    if number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    loaded_bars = some_number // 10
    remaining_bars = 10 - loaded_bars
    return f"{some_number}% [{loaded_bars * '%'}{remaining_bars * '.'}]\nStill loading..."


number = int(input())
print(loading_bar(number))