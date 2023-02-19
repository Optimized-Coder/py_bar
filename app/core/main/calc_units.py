from ..data.cocktails import *

def calculate_units(cocktail):
    total_units = 0
    for ingredient, amount in cocktail.ingredients.items():
        if isinstance(ingredient, Spirit):
            print(ingredient.name, ingredient.ABV)
            total_units += ingredient.ABV * amount / 1000
    return total_units