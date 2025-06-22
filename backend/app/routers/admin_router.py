from fastapi import APIRouter, Depends
from app.dependencies import admin_required
from app.services.cards_service import CardService


router = APIRouter(prefix="/admin")
service = CardService()


@router.get("/dashboard")
def admin_dashboard(user=Depends(admin_required)):
    return {"message": f"Bem vindo ao painel admin, usuário {user['id']}"}


@router.get("/top-selling-cards")
def top_selling_cards():
    return service.get_top_selling_cards()