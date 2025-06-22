from fastapi import APIRouter, HTTPException, status, Path, Body
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
        raise HTTPException(status_code=500, detail=str("e"))
    

@router.put("/update_quantity/{item_id}")
def update_cart_item_quantity(item_id: int, quantity: int = Body(..., embed=True)):
    """
    Atualiza a quantidade de um item no carrinho.
    """
    try:
        cart_service.update_cart_item_quantity(item_id, quantity)
        return {"message": "Quantidade atualizada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.post("/checkout/{user_id}", status_code=status.HTTP_201_CREATED)
def checkout(user_id: int):
    """
    Finaliza o pedido do carrinho ativo do usuário:
    - Valida estoque suficiente
    - Cria pedido
    - Atualiza estoque
    - Marca carrinho como completed
    """
    try:
        cart_service.checkout_cart(user_id)
        return {"message": "Pedido finalizado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))