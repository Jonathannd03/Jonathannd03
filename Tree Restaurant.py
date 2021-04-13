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


kongo_Rstrt = Restaurant('Chez ya Mado', 'kongolesiches')
frankreich_Rstrt = Restaurant('Ratatouille', 'französisches')
spanien_Rstrt = Restaurant('Bilbao', 'spanisches')

kongo_Rstrt.describe_restaurant()
print('\n')

frankreich_Rstrt.describe_restaurant()
print('\n')

spanien_Rstrt.describe_restaurant()

