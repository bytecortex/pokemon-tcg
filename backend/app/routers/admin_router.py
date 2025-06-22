from fastapi import APIRouter, Depends
from app.dependencies import admin_required

router = APIRouter(prefix="/admin")

@router.get("/dashboard")
def admin_dashboard(user=Depends(admin_required)):
    return {"message": f"Bem vindo ao painel admin, usuário {user['id']}"}
