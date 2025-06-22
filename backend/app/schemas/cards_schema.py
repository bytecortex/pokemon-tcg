from pydantic import BaseModel
from typing import Optional

class CardImage(BaseModel):
    small: str
    large: str

class CardSchema(BaseModel):
    id: str
    supertype: str
    subtypes: str
    name: str
    images: CardImage
    series: str
    rarity: Optional[str]
    price: float
    stock: int
    hp: int
    types: str
    flavor_text: Optional[str]

class CardInOrder(BaseModel):
    card_id: str
    name: str
    image_url_small: str
    quantity: int