from fastapi import APIRouter, Depends, HTTPException, status, Path, Body
from typing import List
from app.schemas.order_schema import OrderOut
from app.dependencies import get_current_user

from app.services.order_service import OrderService
from app.db.order_repository import OrderRepository
from app.schemas.cards_schema import CardInOrder


router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/history", response_model=List[OrderOut])
def get_order_history(current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    repo = OrderRepository()
    service = OrderService(repo)
    try:
        orders = service.get_order_history(user_id)
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{order_id}/cards", response_model=List[CardInOrder])
def get_cards_by_order_id(order_id: int, current_user: dict = Depends(get_current_user)):
    repo = OrderRepository()
    service = OrderService(repo)
    try:
        return service.get_cards_by_order_id(order_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))