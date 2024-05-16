import unittest
from unittest.mock import MagicMock, patch
from lib.recipe_normalizer import RecipeNormalizer

class TestRecipeNormalizer(unittest.TestCase):

    def setUp(self):
        self.normalizer = RecipeNormalizer()

    def test_convert_units(self):
        # Test conversion from oz to g
        result = self.normalizer.convert_units(8, "oz", "g")
        self.assertAlmostEqual(result, 226.796, places=3)

        # Test conversion from lb to g
        result = self.normalizer.convert_units(2, "lb", "g")
        self.assertAlmostEqual(result, 907.185, places=3)

        # Test conversion from g to g
        result = self.normalizer.convert_units(500, "g", "g")
        self.assertEqual(result, 500)

        # Test conversion when from_unit is None
        result = self.normalizer.convert_units(100, None, "g")
        self.assertEqual(result, 100)

    def test_normalize_recipe(self):
        # Create a mock recipe_data object
        recipe_data = MagicMock()
        recipe_data.copy.return_value = recipe_data
        recipe_data.ingredients = [{
            "item": "Flour",
            "quantity": 16,
            "unit": "oz",
            "comment": "All-purpose"
        }]

        # Normalize recipe
        normalized_recipe = self.normalizer.normalize_recipe(recipe_data)

        # Check the normalized recipe
        self.assertEqual(len(normalized_recipe["ingredients"]), 1)
        self.assertEqual(normalized_recipe["ingredients"][0]["item"], "Flour")
        self.assertAlmostEqual(normalized_recipe["ingredients"][0]["quantity"], 453.592, places=3)
        self.assertEqual(normalized_recipe["ingredients"][0]["unit"], "g")
        self.assertEqual(normalized_recipe["ingredients"][0]["comment"], "All-purpose")

if __name__ == '__main__':
    unittest.main()