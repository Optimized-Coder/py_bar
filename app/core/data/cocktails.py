from .models import Cocktail, cocktail_list
from .ingredients import *


# COCKTAIL MODEL

# name, 
# ingredients <dict>, 
# glass,
# garnish, 
# method, 
# price

# USE Cocktail.append_cocktail()

# ingreients are instances of Ingredient to add extra properties and functionaility
# first Cocktail.ingredient must be base spirit

margarita = Cocktail(
    'Margarita', 
    {
        tequila: 50,
        triple_sec: 20,
        lime_juice: 20,
        gomme: 10
    },
    'Coupe',
    'Lime Wheel',
    'shaken', 
)

margarita.append_cocktail()

singapore_sling = Cocktail(
    'Singapore Sling',
    {
        gin: 30,
        cointreau: 7.5,
        lime_juice: 15,
        pineapple_juice: 120,
        grenadine: 10,
        angustura_bitters: 1,
        cherry_liqueur: 15,
        dom_benedictine: 7.5
    },
    'Sling',
    'Cherry',
    'shaken',
)
singapore_sling.append_cocktail()

mojito = Cocktail(
    'Mojito',
    {
        white_rum: 50,
        mint: 10,
        lime_juice: 25,
        gomme: 25,
        soda: 1 
    },
    'Collins',
    'Mint Sprig',
    'built',
)
mojito.append_cocktail()

vesper = Cocktail(
    'Vesper',
    {
        gin: 45,
        vodka: 15,
        lillet_blanc: 7.5
    },
    'Martini',
    'Lemon Twist',
    'shaken', 
)
vesper.append_cocktail()



