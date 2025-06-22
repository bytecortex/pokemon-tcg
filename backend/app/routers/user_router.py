from fastapi import APIRouter, Depends
from app.db.user_repository import UserRepository
from app.schemas.user_schema import UserResponse

router = APIRouter()
repo = UserRepository()

@router.get("/users", response_model=list[UserResponse])
def get_users():
    return repo.get_all_users()