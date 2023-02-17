from menu import view_menu
from cocktails import *

view_menu()

margarita.make_cocktail()

print('=== Margarita ===')
print(f'Cost: £{margarita.calculate_cost():.2f}')
print(f'Profit: £{margarita.calculate_profit():.2f}')

