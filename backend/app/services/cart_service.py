from typing import List
from app.schemas.cart_schema import CartSchema, CartItemSchema
from app.db.cart_repository import CartRepository


class CartService:
    def __init__(self):
        self.repository = CartRepository()

    def get_or_create_cart(self, user_id: int) -> CartSchema:
        cart_id = self.repository.get_or_create_active_cart(user_id)
        return CartSchema(
            id=cart_id,
            user_id=user_id,
            status='active',
            created_at=None,   
            updated_at=None
        )
    
    def add_item_to_cart(self, user_id: int, card_id: str) -> None:
        self.repository.add_card_to_cart(user_id, card_id)

    def list_cart_items(self, user_id: int) -> List[CartItemSchema]:
        items = self.repository.list_cart_items(user_id)
        return [CartItemSchema(**item) for item in items]

    def update_cart_item_quantity(self, item_id: int, quantity: int) -> None:
        self.repository.update_cart_item_quantity(item_id, quantity)