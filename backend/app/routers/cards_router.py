from fastapi import APIRouter, Query
from typing import Optional, List
from app.schemas.cards_schema import CardSchema
from app.services.cards_service import CardService

router = APIRouter(prefix="/cards", tags=["Cards"])
card_service = CardService()

@router.get("", response_model=List[CardSchema])
def get_cards(
    name: Optional[str] = Query(None, description="Nome do card"),
    types: Optional[str] = Query(None, description="Tipo do card"),
    limit: int = Query(30, ge=1, le=100, description="Limite de resultados"),
    in_stock_only: bool = Query(False, description="Filtrar somente cartas com estoque")
):
    return card_service.list_cards(name=name, types=types, limit=limit, in_stock_only=in_stock_only)
