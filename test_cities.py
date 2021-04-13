import unittest

from city_function import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = city_country("Beni", "Kongo")
        self.assertEqual(formatted_name, "Beni,Kongo.")

    def test_city_country_population(self):
        formatted_name = city_country("Beni", "Kongo", "700000")
        self.assertEqual(formatted_name, "Beni,Kongo,Population:700000.")

if __name__ == '__main__':
    unittest.main()