# Cocktail class 
# Accepts name, ingredients dict with quantities, glass, garnish, method, price and a description
cocktail_list = []

class Cocktail():

    

    def __init__(
        self, name, ingredients, glass, garnish, method, price
        ):
        self.name = name
        self.ingredients = ingredients
        self.glass = glass
        self.garnish = garnish
        self.method = method
        self.price = price
    
    def __repr__(self) -> str:
        return self.name
    
    def append_cocktail(self):
        cocktail_list.append(self)
    
    def make_cocktail(self):
        print('=========')
        print(f'Making your {self.name}')
        if self.method == 'shaken':
            for ingredient, amount in self.ingredients.items():
                print(f'Add {amount}ml {ingredient} to tin')
            print('Add ice and shake until chilled')
        print(f'Pour into a {self.glass}')
        print(f'Garnish with a {self.garnish}')
        print(f'Here is your {self.name}, that\'ll be £{self.price:.2f}')
        print('=========')
    
    def calculate_cost(self):
        cost = 0
        for ingredient, amount in self.ingredients.items():
            cost += ingredient.price_per_unit * amount
        return cost

    def calculate_profit(self):
        return self.price * 0.8 - self.calculate_cost()


# ingredients for each cocktail

ingredient_list = []

class Ingredient():
    def __init__(self, name, price_each, unit, num_of_units):
        self.name = name
        # price per btl
        self.price_each = price_each 
        # unit
        self.unit = unit
        # number of ml
        self.num_of_units = num_of_units

        # price per ml
        self.price_per_unit = self.price_each / self.num_of_units

    def append_ingredient(self):
        ingredient_list.append(self)

    def __repr__(self) -> str:
        return f'{self.name}'

class Spirit(Ingredient):
    def __init__(self, name, price_each, unit, num_of_units, ABV):
        super().__init__(name, price_each, unit, num_of_units)
        self.ABV = ABV

