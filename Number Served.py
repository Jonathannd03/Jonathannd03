class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """printet attributen"""
        print('\t', self.restaurant_name, 'Restaurant.')
        print('\t', 'Das beste', self.cuisine_type, 'Essen Deutschlands.')

    def open_restaurant(self):
        """öffnet das Restaurant"""
        print('\t', self.restaurant_name, ' ist jetzt geöffnet. :)')

    def check_number(self):
        """printet die bedienten Gäste"""
        print('\t Das Restaurant hat heute', str(self.number_served), 'bedient')

    def set_number_served(self, number_served):
        self.number_served = number_served
        print('\t', self.number_served, 'Gäste haben ihr Essen bekommen')
        return self.number_served

    def increment_number_served(self, increment):
        self.number_served += increment
        print('\t', increment, 'Leute sind zusätzlich bedient worden, also Heute haben wir', self.number_served, 'bedient')

restaurant = Restaurant('Milanito', 'italienische')
print('\n\tDer Name des Restaurants ist ', restaurant.restaurant_name, '.')
print('\tEs bietet ', restaurant.cuisine_type, ' Essen.')

print('\n')

restaurant.open_restaurant()
restaurant.describe_restaurant()
restaurant.set_number_served(38)
restaurant.increment_number_served(64)


