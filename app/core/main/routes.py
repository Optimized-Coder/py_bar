from flask import render_template, url_for
from . import bp
from ..data.cocktails import *

def calculate_units(cocktail):
    total_units = 0
    for ingredient, amount in cocktail.ingredients.items():
        if isinstance(ingredient, Spirit):
            print(ingredient.name, ingredient.ABV)
            total_units += ingredient.ABV * amount / 1000
    return total_units

print(calculate_units(mojito))

@bp.route('/')
@bp.route('/home/')
def home():
    context = {
        'title': 'Menu',
        'cocktail_list': cocktail_list,
        'calculate_units': calculate_units
    }

    return render_template(
        'index.html', 
        **context
    )