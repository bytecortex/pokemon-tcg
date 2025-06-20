from pydantic import BaseModel
from typing import Optional

class CardImage(BaseModel):
    small: str
    large: str

class CardSchema(BaseModel):
    id: str
    name: str
    images: CardImage
    series: str
    rarity: Optional[str]
    price: float
