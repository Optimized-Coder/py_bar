class Cocktail():
    def __init__(
        self, 
        name, 
        ingredients, 
        glass, 
        garnish,
        method,
        price
        ):
        self.name = name
        self.ingredients = ingredients
        self.glass = glass
        self.garnish = garnish
        self.method = method
        self.price = price
    
    def make_cocktail(self):
        print('=========')
        print(f'Making your {self.name}')
        if self.method == 'shaken':
            for ingredient, amount in self.ingredients.items():
                print(f'Add {amount}ml {ingredient} to tin')
            print('Add ice and shake until chilled')
        print(f'Pour into a {self.glass}')
        print(f'Garnish with a {self.garnish}')
        print(f'Here is your {self.name}, that\'ll be £{self.price}')
        print('=========')