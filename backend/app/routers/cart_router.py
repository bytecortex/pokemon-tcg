from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.cart_schema import CartItemSchema, AddToCartRequest
from app.services.cart_service import CartService
import traceback

router = APIRouter(prefix="/cart", tags=["Cart"])
cart_service = CartService()


@router.post("/add", status_code=201)
def add_to_cart(data: AddToCartRequest):
    """
    Adiciona uma carta ao carrinho ativo do usuário.
    """
    try:
        cart_service.add_item_to_cart(user_id=data.user_id, card_id=data.card_id)
        return {"message": "Carta adicionada ao carrinho com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/items/{user_id}", response_model=List[CartItemSchema])
def get_cart_items(user_id: int):
    """
    Retorna os itens do carrinho ativo de um usuário.
    """
    try:
        return cart_service.list_cart_items(user_id)
    except Exception as e:
        print(f"Erro no test-cart: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str("e"))
    

@router.put("/items/{user_id}/{card_id}")
def update_quantity(user_id: int, card_id: str):
    """
    Adiciona nova quantidade de um item ao carrinho.
    """
    try:
        return cart_service.add_item_to_cart(user_id, card_id)
    except Exception as e:
        print(f"Erro no test-cart: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str("e"))
