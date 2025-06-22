from fastapi import APIRouter, Depends
from app.db.user_repository import UserRepository
from app.db.order_repository import OrderRepository
from app.services.dashboard_service import DashboardService  # supondo que criou o serviço

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def get_dashboard():
    user_repo = UserRepository()
    order_repo = OrderRepository()
    service = DashboardService(user_repo, order_repo)
    data = service.get_dashboard_data()
    return data
