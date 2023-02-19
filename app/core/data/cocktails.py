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
    7.00
)

margarita.append_cocktail()

singapore_sling = Cocktail(
    'Singapore Sling',
    {
        cointreau: 7.5,
        lime_juice: 15,
        pineapple_juice: 120,
        gin: 30,
        grenadine: 10,
        angustura_bitters: 1,
        cherry_liqueur: 15,
        dom_benedictine: 7.5
    },
    'Sling',
    'Cherry',
    'shaken',
    9.50
)
singapore_sling.append_cocktail()

mojito = Cocktail(
    'Mojito',
    {
        mint: 10,
        lime_juice: 25,
        gomme: 25,
        white_rum: 50,
        soda: 1 
    },
    'Collins',
    'Mint Sprig',
    'built',
    9.00
)
mojito.append_cocktail()





