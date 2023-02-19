from flask import render_template, url_for
from . import bp
from ..data.cocktails import *

@bp.route('/')
@bp.route('/home/')
def home():
    context = {
        'title': 'Menu',
        'cocktail_list': cocktail_list
    }

    return render_template(
        'index.html', **context 
    )