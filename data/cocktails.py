from models import Cocktail

margarita = Cocktail(
    'Margarita', 
    {
        'Tequila': 50,
        'Triple Sec': 20,
        'Lime Juice': 20,
        'Gomme': 10
    },
    'Coupe',
    'Lime Wheel',
    'shaken', 
    7.00
)

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

cocktail_list = [margarita, singapore_sling]
