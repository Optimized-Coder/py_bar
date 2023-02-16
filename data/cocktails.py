from models import Cocktail

margarita = Cocktail(
    'Margarita', 
    [
        {'Tequila': 50}, 
        {'Lime': 25}, 
        {'Sugar', 25},
        {'Triple sec': 20}
        ],
    'Coupe',
    'Lime Wheel',
    'shaken', 
    7.00
)

cocktail_list = [margarita]
