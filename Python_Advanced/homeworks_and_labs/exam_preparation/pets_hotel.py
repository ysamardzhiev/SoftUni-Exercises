def accommodate_new_pets(capacity: int, max_weight: float, *pets):
    accommodated_pets = {}
    result = ''

    for pet, weight in pets:
        if not capacity:
            result += "You did not manage to accommodate all pets!\n"
            break
        if weight > max_weight:
            continue

        accommodated_pets.setdefault(pet, 0)
        accommodated_pets[pet] += 1
        capacity -= 1
    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += 'Accommodated pets:\n'

    for pet, quantity in sorted(accommodated_pets.items()):
        result += f'{pet}: {quantity}\n'

    return result



print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


