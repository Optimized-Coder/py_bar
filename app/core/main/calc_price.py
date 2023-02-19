def calculate_cost(cocktail):
        cost = 0
        for ingredient, amount in cocktail.ingredients.items():
            cost += ingredient.price_per_unit * amount
        return cost

gross_profit_margin = 0.75

def calculate_price(cocktail):
    price = cocktail.calculate_cost() / (1 - gross_profit_margin)
    return round(price, 1)