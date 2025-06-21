from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class CartSchema(BaseModel):
    id: int
    user_id: int
    status: Literal['active', 'completed', 'cancelled']
    created_at: datetime
    updated_at: datetime


class CartItemSchema(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    image_url: Optional[str] = None


class AddToCartRequest(BaseModel):
    user_id: int
    card_id: str


