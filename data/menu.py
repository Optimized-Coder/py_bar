from cocktails import cocktail_list

def view_menu():
    print('==========')
    print('Here is the menu: ')
    for cocktail in cocktail_list:
        print(cocktail.name, cocktail.price)
    print('==========')