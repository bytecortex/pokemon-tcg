from fastapi import HTTPException
from passlib.hash import bcrypt
from app.db.user_repository import UserRepository
from app.core.security import create_access_token 

class AuthService:
    def __init__(self):
        self.repo = UserRepository()

    def login(self, email: str, password: str):
        user = self.repo.find_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="Email not found")

        user_id, name, hashed_password, role = user  # role agora vem do banco
        if not bcrypt.verify(password, hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect password")

        access_token = create_access_token(
            data={"id": user_id, "name": name, "email": email, "role": role}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user_id,
                "name": name,
                "email": email,
                "role": role,
            },
        }

    def register(self, name: str, email: str, password: str):
        if self.repo.email_exists(email):
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed = bcrypt.hash(password)
        self.repo.create_user(name, email, hashed)
