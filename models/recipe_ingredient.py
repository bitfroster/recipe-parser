from pydantic import BaseModel, Field, field_validator
from typing import Optional


class RecipeIngredient(BaseModel):
    item: str
    quantity: float
    unit: Optional[str] = None
    comment: Optional[str] = None

    @field_validator('unit')
    def convert_unit_to_lowercase(cls, values):
        if values is not None and values.strip():
            return values.lower()