def sorting_cheeses(**kwargs):
    result = ''
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for cheese, quantities in sorted_result:
        result += cheese + '\n'
        for quantity in sorted(quantities, reverse=True):
            result += f'{quantity}\n'
    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

