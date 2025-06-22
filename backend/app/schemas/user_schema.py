from datetime import datetime
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

class UserWithOrdersResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    total_orders: int
    