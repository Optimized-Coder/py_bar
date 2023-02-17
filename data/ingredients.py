from models import Ingredient, ingredient_list, Spirit

# Ingredient Model
# - name
# - cost each divisible unit
# - measurable unit
# - num of measurable units



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

tequila = Spirit(
    'Tequila',
    17.5,
    'ml',
    700,
    0.375
)
tequila.append_ingredient()

cointreau = Ingredient(
    'Cointreau',
    12,
    'ml',
    700
)
cointreau.append_ingredient()

pineapple_juice = Ingredient(
    'Pineapple Juice',
    1.5,
    'ml',
    1000
)
pineapple_juice.append_ingredient()

gin = Spirit(
    'Gin',
    20,
    'ml',
    700
)
gin.append_ingredient()

grenadine = Ingredient(
    'Grenadine',
    2.5,
    'ml',
    700
)
grenadine.append_ingredient()

angustura_bitters = Spirit(
    'Angustura Bitters',
    5,
    'dash',
    700,
    0.35
)
angustura_bitters.append_ingredient()