from .models import Ingredient, ingredient_list, Spirit

# Ingredient Model
# - name
# - cost each divisible unit
# - measurable unit
# - num of measurable units

# Spirit() subclass also has Spirit.ABV

# use Spirit.append_ingredient() after creating each instance

                    # =========Spirits =========
tequila = Spirit(
    'Tequila',
    20,
    'ml',
    700,
    38
)
tequila.append_ingredient()

gin = Spirit(
    'Gin',
    15.99,
    'ml',
    700,
    44
)
gin.append_ingredient()

cointreau = Spirit(
    'Cointreau',
    16.75,
    'ml',
    700,
    40
)
cointreau.append_ingredient()

angustura_bitters = Spirit(
    'Angustura Bitters',
    10,
    'dash',
    700,
    44.7
)
angustura_bitters.append_ingredient()

cherry_liqueur = Spirit(
    'Cherry Liqueur',
    19.9,
    'ml',
    700,
    24
)
cherry_liqueur.append_ingredient()

dom_benedictine = Spirit(
    'DOM Benedictine',
    18,
    'ml',
    700,
    40
)
dom_benedictine.append_ingredient()

white_rum = Spirit(
    'White Rum',
    14,
    'ml',
    700,
    40
)
white_rum.append_ingredient()

triple_sec = Spirit(
    'Triple Sec',
    15.99,
    'ml',
    700,
    20
)
triple_sec.append_ingredient()

vodka = Spirit(
    'Vodka',
    13.99,
    'ml',
    700,
    40
)
vodka.append_ingredient()

lillet_blanc = Spirit(
    'Lillet Blanc',
    18.99,
    'ml',
    700,
    17
)
lillet_blanc.append_ingredient()

                    # =========Defualt ingredients =========
# use Ingredient.append_ingredient() after creating each instance
lime_juice = Ingredient(
    'Lime Juice',
    35,
    'ml',
    500
)
lime_juice.append_ingredient()

gomme = Ingredient(
    'Gomme',
    4,
    'ml',
    700
)
gomme.append_ingredient()


pineapple_juice = Ingredient(
    'Pineapple Juice',
    1.5,
    'ml',
    1000
)
pineapple_juice.append_ingredient()

grenadine = Ingredient(
    'Grenadine',
    2.5,
    'ml',
    700
)
grenadine.append_ingredient()

mint = Ingredient(
    'Mint',
    1,
    'leaves',
    75
)
mint.append_ingredient()

soda = Ingredient(
    'Soda',
    0,
    'dash',
    1
)
soda.append_ingredient()
