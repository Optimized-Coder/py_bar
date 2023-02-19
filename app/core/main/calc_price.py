# change this to be your desired GP
gross_profit_margin = 0.75


# uses calculate cost method on cocktail class and disired gp
# for dynamic pricing
def calculate_price(cocktail):
    price = cocktail.calculate_cost() / (1 - gross_profit_margin)
    return round(price, 1)