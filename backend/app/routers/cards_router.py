from fastapi import APIRouter, HTTPException, Path, Query
from typing import Optional, List
from app.schemas.cards_schema import CardSchema, CardUpdateRequest
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

@router.get("/{card_id}", response_model=CardSchema)
def get_card_by_id(card_id: str = Path(..., description="ID da carta")):
    try:
        return card_service.get_card_by_id(card_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Carta não encontrada")

@router.put("/{card_id}")
def update_card(card_id: str, data: CardUpdateRequest):
    try:
        card_service.update_card(card_id, data)
        return {"message": "Carta atualizada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))