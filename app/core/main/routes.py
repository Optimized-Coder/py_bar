from flask import render_template, url_for
from . import bp
from ..data.cocktails import *
from .calc_units import calculate_units

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