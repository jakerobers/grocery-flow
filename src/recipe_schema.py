from typing import List, Optional
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str  # g, pcs, etc.
    preparation: Optional[str] = ""  # chopped, minced, etc.
    optional: bool = False


@dataclass
class Recipe:
    title: str
    description: str
    ingredients: List[Ingredient]
    instructions: List[str]
