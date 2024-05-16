import xml.etree.ElementTree as ET
from models.recipe_ingredient import RecipeIngredient
from models.recipe import Recipe
from pydantic import ValidationError


class XMLRecipeParser:
    def parse_file(self, file_path):
        try:
            tree = ET.parse(file_path)
        except ET.ParseError as e:
            print(f"Error parsing file {file_path}: {e}")
            return None

        root = tree.getroot()

        name = root.find("name").text
        ingredients = []
        for ingredient_elem in root.findall("ingredients"):
            item = ingredient_elem.find("item").text
            quantity = float(ingredient_elem.find("quantity").text)
            unit = ingredient_elem.find("unit").text or ""
            comment = (
                ingredient_elem.find("comment").text
                if ingredient_elem.find("comment") is not None
                else None
            )
            try:
                ingredients.append(
                    RecipeIngredient(
                        item=item, quantity=quantity, unit=unit, comment=comment
                    )
                )
            except ValidationError as e:
                print(f"Error parsing ingredient in {file_path}: {e}")
                continue

        preperations = [prep.text for prep in root.findall("preperations")]

        return Recipe(name=name, ingredients=ingredients, preperations=preperations)
