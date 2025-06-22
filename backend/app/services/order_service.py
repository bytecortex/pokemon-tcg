from typing import List
from app.db.order_repository import OrderRepository
from app.schemas.order_schema import OrderOut

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def get_order_history(self, user_id: int) -> List[OrderOut]:
        rows = self.order_repository.get_order_history(user_id)
        orders = [
            OrderOut(id=row["id"], created_at=row["created_at"], total_price=row["total_price"])
            for row in rows
        ]
        return orders
