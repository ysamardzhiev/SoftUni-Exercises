def concatenate(*args, **kwargs):
    result = ''.join(args)

    for key, string in kwargs.items():
        result = result.replace(key, string)

    return ''.join(result)


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))