from models import Cocktail, cocktail_list
from ingredients import *

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
        'Cointreau': 7.5,
        'Lime juice': 15,
        'Pineapple Juice': 120,
        'Gin': 30,
        'Grenadine': 10,
        'Angustura bitters': 1,
        'Cherry Liqueur': 15,
        'DOM Benedictine': 7.5
    },
    'Sling',
    'Cherry',
    'shaken',
    9.50
)
singapore_sling.append_cocktail()





