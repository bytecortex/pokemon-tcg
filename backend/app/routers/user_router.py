from fastapi import APIRouter, Depends, Query
from app.db.user_repository import UserRepository
from app.schemas.user_schema import UserResponse, UserWithOrdersResponse

router = APIRouter()
repo = UserRepository()

@router.get("/users", response_model=list[UserResponse])
def get_users():
    return repo.get_all_users()

@router.get("/users-orders", response_model=list[UserWithOrdersResponse])
def get_users_with_orders(name: str = Query("")):
    return repo.get_users_with_orders_by_name(name)