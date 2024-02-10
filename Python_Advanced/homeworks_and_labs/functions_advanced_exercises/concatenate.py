def concatenate(*args, **kwargs):
    result = ''

    for el in args:
        result += el

    for key, string in kwargs.items():
        if key in result:
            result = result.replace(key, string)

    return ''.join(result)


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))