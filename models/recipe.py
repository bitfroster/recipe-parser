from typing import List, Optional
from pydantic import BaseModel
from .recipe_ingredient import RecipeIngredient


class Recipe(BaseModel):
    name: str
    ingredients: List[RecipeIngredient]
    preperations: Optional[str] = None
