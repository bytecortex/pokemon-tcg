from pydantic import BaseModel
from typing import Optional

class CardImage(BaseModel):
    small: str

class CardSet(BaseModel):
    name: str
    id: Optional[str] = ""

class CardSchema(BaseModel):
    id: str
    name: str
    images: CardImage
    set: CardSet
