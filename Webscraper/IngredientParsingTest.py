import unittest
from IngredientList import split_ingredient  

class TestSplitIngredient(unittest.TestCase):

    def test_regular_measurement(self):
        ingredient = '75g/2½oz self-raising flour'
        expected_output = ('75g/21/2oz', 'Self-raising Flour')
        self.assertEqual(split_ingredient(ingredient), expected_output)

    def test_ingredient_with_standalone_number(self):
        ingredient = '4 eggs'
        expected_output = ('4', 'Eggs')
        self.assertEqual(split_ingredient(ingredient), expected_output)

    def test_ingredient_with_longform_unit(self):
        ingredient = '1 litre/1¾ pints vegetable stock'
        expected_output = ('1 litre/13/4 pints', 'Vegetable Stock')
        self.assertEqual(split_ingredient(ingredient), expected_output)

    def test_ingredient_with_unicode_fraction(self):
        ingredient = '½ tsp salt'
        expected_output = ('1/2 tsp', 'Salt')
        self.assertEqual(split_ingredient(ingredient), expected_output)

    def test_ingredient_with_unknown_quantity(self):
        ingredient = 'some olive oil'
        expected_output = ('Unknown quantity', 'Some Olive Oil')
        self.assertEqual(split_ingredient(ingredient), expected_output)

    # Add more tests for edge cases and different scenarios...

if __name__ == '__main__':
    unittest.main()
