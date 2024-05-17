from typing import List
from pydantic import BaseModel
from .recipe_ingredient import RecipeIngredient


class Recipe(BaseModel):
    name: str
    ingredients: List[RecipeIngredient]
    preperations: List[str] | None
