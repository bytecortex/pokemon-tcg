from fastapi import APIRouter
from app.schemas.user import LoginRequest, RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

@router.post("/login")
def login(data: LoginRequest):
    user = auth_service.login(data.email, data.password)
    return {"message": "Login successful", "user": user}

@router.post("/register")
def register(data: RegisterRequest):
    auth_service.register(data.name, data.email, data.password)
    return {"message": "User successfully registered"}
