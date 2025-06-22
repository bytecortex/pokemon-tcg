from typing import List
from app.schemas.cart_schema import CartSchema, CartItemSchema
from app.db.cart_repository import CartRepository


class CartService:
    def __init__(self):
        self.repository = CartRepository()

    def get_or_create_cart(self, user_id: int) -> CartSchema:
        cart_id = self.repository.get_or_create_active_cart(user_id)
        return CartSchema(
            id=cart_id,
            user_id=user_id,
            status='active',
            created_at=None,   
            updated_at=None
        )
    
    
    def add_item_to_cart(self, user_id: int, card_id: str) -> None:
        self.repository.add_card_to_cart(user_id, card_id)


    def list_cart_items(self, user_id: int) -> List[CartItemSchema]:
        items = self.repository.list_cart_items(user_id)
        return [CartItemSchema(**item) for item in items]


    def update_cart_item_quantity(self, item_id: int, quantity: int) -> None:
        self.repository.update_cart_item_quantity(item_id, quantity)


    def checkout_cart(self, user_id: int) -> None:
        # Obter o carrinho ativo e seus itens
        cart_id = self.repository.get_or_create_active_cart(user_id)
        items = self.repository.list_cart_items(user_id)

        if not items:
            raise Exception("Carrinho vazio.")

        # Validar estoque para cada item
        for item in items:
            stock = self.repository.get_card_stock(item["card_id"])
            if stock < item["quantity"]:
                raise Exception(
                    f"Estoque insuficiente para {item['name']}.\nDisponível: {stock}\nPedido: {item['quantity']}"
                )

        # Calcular preço total
        total_price = sum(item["price"] * item["quantity"] for item in items)

        # Criar pedido e atualizar status carrinho + atualizar estoque em transaction
        self.repository.create_order_and_complete_cart(cart_id, user_id, total_price)
