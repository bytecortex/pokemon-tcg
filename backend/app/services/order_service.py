from typing import List
from app.db.order_repository import OrderRepository
from app.schemas.order_schema import OrderOut
from app.schemas.cards_schema import CardInOrder

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def get_order_history(self, user_id: int) -> List[OrderOut]:
        rows = self.order_repository.get_order_history(user_id)
        return [OrderOut(**row) for row in rows]

    def get_cards_by_order_id(self, order_id: int) -> List[CardInOrder]:
        rows = self.order_repository.get_cards_by_order_id(order_id)
        return [CardInOrder(**row) for row in rows]