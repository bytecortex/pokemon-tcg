from app.db.user_repository import UserRepository
from app.db.order_repository import OrderRepository


class DashboardService:
    def __init__(self, user_repo: UserRepository, order_repo: OrderRepository):
        self.user_repo = user_repo
        self.order_repo = order_repo


    def get_dashboard_data(self) -> dict:
        total_users = self.user_repo.get_total_users()
        order_data = self.order_repo.get_total_orders_and_revenue()
        return {
            "totalUsers": total_users,
            "totalOrders": order_data["total_orders"],
            "totalRevenue": order_data["total_revenue"]
        }