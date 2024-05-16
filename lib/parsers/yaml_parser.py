import yaml
from models.recipe_ingredient import RecipeIngredient
from models.recipe import Recipe
from pydantic import ValidationError


class YAMLRecipeParser:
    def parse_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error parsing file {file_path}: {e}")
            return None

        if not isinstance(data, dict):
            print(f"Error parsing file {file_path}: Invalid YAML format")
            return None

        name = data.get("name")
        ingredients = []
        for ingredient in data.get("ingredients", []):
            if not isinstance(ingredient, dict):
                print(
                    f"Error parsing ingredient in {file_path}: Invalid ingredient format"
                )
                continue
            try:
                ingredients.append(RecipeIngredient(**ingredient))
            except ValidationError as e:
                print(f"Error parsing ingredient in {file_path}: {e}")
                continue

        preperations = data.get("preperations")

        return Recipe(name=name, ingredients=ingredients, preperations=preperations)
