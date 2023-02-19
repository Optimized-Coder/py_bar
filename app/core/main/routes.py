from flask import render_template, url_for
from . import bp
from ..data.cocktails import *
from .calc_units import calculate_units
from .calc_price import calculate_price

# 2 + .80 = 10 / 10


@bp.route('/')
@bp.route('/home/')
def home():
    context = {
        'title': 'Menu',
        'cocktail_list': cocktail_list,
        'calculate_units': calculate_units,
        'calculate_price': calculate_price
    }

    return render_template(
        'index.html', 
        **context
    )