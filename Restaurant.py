class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """print attributes"""
        print('\t', self.restaurant_name, 'Restaurant.')
        print('\t', 'Das beste', self.cuisine_type, 'Essen Deutschlands.')

    def open_restaurant(self):
        """opens the restaurant"""
        print('\t', self.restaurant_name, ' ist jetzt geöffnet. :)')

restaurant = Restaurant('Milanito', 'Italienisches')
print('\n\tDer Name des Restaurants ist ', restaurant.restaurant_name, '.')
print('\tEs bietet ', restaurant.cuisine_type, ' Essen.')

print('\n')

restaurant.open_restaurant()
restaurant.describe_restaurant()
