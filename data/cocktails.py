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

cocktail_list = [margarita]
