def cookbook(*args):
    cuisines = {}

    for recipe_name, cuisine, ingredients in args:
        cuisines.setdefault(cuisine, [])
        cuisines[cuisine].append((recipe_name, ingredients))

    sorted_cuisines = sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for cuisine, recipes in sorted_cuisines:
        result += f'{cuisine} cuisine contains {len(recipes)} recipes:\n'
        sorted_recipes = sorted(recipes, key=lambda x: x[0])
        for recipe in sorted_recipes:
            result += f'  * {recipe[0]} -> Ingredients: {", ".join(recipe[1])}\n'

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
