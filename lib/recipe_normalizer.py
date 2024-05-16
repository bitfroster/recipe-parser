import json
import os
from models.recipe_ingredient import RecipeIngredient
from pint import UnitRegistry
from config import config
from lib.parsers.xml_parser import XMLRecipeParser
from lib.parsers.yaml_parser import YAMLRecipeParser


class RecipeNormalizer:
    def __init__(self):
        self.__parsers = {".xml": XMLRecipeParser(), ".yaml": YAMLRecipeParser()}
        self.__ureg = UnitRegistry()

    def convert_units(self, amount, from_unit, to_unit):
        return self.__ureg.Quantity(amount, from_unit).to(to_unit).magnitude

    def normalize_recipe(self, recipe):
        normalized_recipe = recipe.copy(
            update={
                "ingredients": [
                    RecipeIngredient(
                        item=ingredient.item,
                        quantity=(
                            self.convert_units(
                                ingredient.quantity, ingredient.unit, "g"
                            )
                            if ingredient.unit.lower() in ["lb", "pound", "pounds"]
                            else ingredient.quantity
                        ),
                        unit=(
                            "g"
                            if ingredient.unit.lower() in ["lb", "pound", "pounds"]
                            else (
                                "ml"
                                if ingredient.unit.lower() in ["oz", "ounce", "ounces"]
                                else ingredient.unit
                            )
                        ),
                        comment=ingredient.comment,
                    )
                    for ingredient in recipe.ingredients
                ]
            }
        )
        return normalized_recipe

    def process_directory(self, directory):
        recipes = []
        for file_name in os.listdir(directory):
            full_file_path = os.path.join(directory, file_name)
            if os.path.isfile(full_file_path):
                extension = os.path.splitext(file_name)[1].lower()
                parser = self.__parsers.get(extension)
                if parser:
                    try:
                        recipe_data = parser.parse_file(full_file_path)
                        if recipe_data is not None:
                            recipe = self.normalize_recipe(recipe_data)
                            recipes.append(recipe.dict())
                    except Exception as e:
                        print(f"Error parsing file {full_file_path}: {e}")
                        continue
                else:
                    print(f"Unsupported file format: {file_name}")

        with open(config.get("output_file", "output_file.json"), "w") as file:
            json.dump(recipes, file, indent=2)
