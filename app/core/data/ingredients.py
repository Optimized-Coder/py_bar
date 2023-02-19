from .models import Ingredient, ingredient_list, Spirit

# Ingredient Model
# - name
# - cost each divisible unit
# - measurable unit
# - num of measurable units

# Spirit() subclass also has Spirit.ABV

# use Ingredient.append_ingredient()  

                    # =========Spirits =========
tequila = Spirit(
    'Tequila',
    17.5,
    'ml',
    700,
    0.375
)
tequila.append_ingredient()

gin = Spirit(
    'Gin',
    20,
    'ml',
    700,
    0.375
)
gin.append_ingredient()

cointreau = Spirit(
    'Cointreau',
    12,
    'ml',
    700,
    0.25
)
cointreau.append_ingredient()

angustura_bitters = Spirit(
    'Angustura Bitters',
    5,
    'dash',
    700,
    0.35
)
angustura_bitters.append_ingredient()

cherry_liqueur = Spirit(
    'Cherry Liqueur',
    15,
    'ml',
    700,
    0.25
)
cherry_liqueur.append_ingredient()

dom_benedictine = Spirit(
    'DOM Benedictine',
    15,
    'ml',
    700,
    0.2
)
dom_benedictine.append_ingredient()

white_rum = Spirit(
    'White Rum',
    18,
    'ml',
    700,
    0.375
)
white_rum.append_ingredient()

                    # =========Defualt ingredients =========

lime_juice = Ingredient(
    'Lime Juice',
    35,
    'ml',
    500
)
lime_juice.append_ingredient()

triple_sec = Ingredient(
    'Triple Sec',
    12,
    'ml',
    700
)
triple_sec.append_ingredient()

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



print(ingredient_list)