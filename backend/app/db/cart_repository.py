from typing import Optional
from app.db.connection import Database
from mysql.connector import Error


class CartRepository:
    def get_or_create_active_cart(self, user_id: int) -> int:
        """
        Busca o carrinho ativo de um usuário. Se não existir, cria um novo.
        Retorna o ID do carrinho.
        """
        db = Database().connect()
        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT id FROM carts WHERE user_id = %s AND status = 'active' LIMIT 1",
                (user_id,)
            )
            cart = cursor.fetchone()

            if cart:
                return cart["id"]

            # Criar novo carrinho
            cursor.execute(
                "INSERT INTO carts (user_id, status, created_at, updated_at) VALUES (%s, 'active', NOW(), NOW())",
                (user_id,)
            )
            db.commit()
            return cursor.lastrowid

        except Error as e:
            db.rollback()
            raise Exception(f"Erro ao buscar/criar carrinho: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def add_card_to_cart(self, user_id: int, card_id: str) -> None:
        """
        Adiciona uma carta ao carrinho ativo do usuário.
        Se a carta já estiver no carrinho, incrementa a quantidade.
        """
        db = Database().connect()
        cursor = db.cursor(dictionary=True)

        try:
            cart_id = self.get_or_create_active_cart(user_id)

            # Verifica se já existe o item no carrinho
            cursor.execute(
                "SELECT id, quantity FROM cart_items WHERE cart_id = %s AND card_id = %s",
                (cart_id, card_id)
            )
            item = cursor.fetchone()

            if item:
                cursor.execute(
                    "UPDATE cart_items SET quantity = quantity + 1 WHERE id = %s",
                    (item["id"],)
                )
            else:
                cursor.execute(
                    "INSERT INTO cart_items (cart_id, card_id, quantity) VALUES (%s, %s, 1)",
                    (cart_id, card_id)
                )

            db.commit()

        except Error as e:
            db.rollback()
            raise Exception(f"Erro ao adicionar carta ao carrinho: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def list_cart_items(self, user_id: int) -> list:
        db = Database().connect()
        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                """
                SELECT
                    ci.id AS id,
                    ci.card_id AS card_id,
                    ci.quantity AS quantity,
                    c.name AS name,
                    c.price AS price,
                    c.image_url_small AS image_url
                FROM cart_items ci
                JOIN carts ca ON ci.cart_id = ca.id
                JOIN cards c ON ci.card_id = c.id
                WHERE ca.user_id = %s AND ca.status = 'active'
                """,
                (user_id,)
            )
            items = cursor.fetchall()
            return items if items else []

        except Error as e:
            raise Exception(f"Erro ao buscar itens do carrinho: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def update_cart_item_quantity(self, item_id: int, quantity: int) -> None:
        db = Database().connect()
        cursor = db.cursor()

        try:
            if quantity < 1:
                # Remove item se a quantidade for 0
                cursor.execute("DELETE FROM cart_items WHERE id = %s", (item_id,))
            else:
                cursor.execute("UPDATE cart_items SET quantity = %s WHERE id = %s", (quantity, item_id))

            db.commit()
        except Error as e:
            db.rollback()
            raise Exception(f"Erro ao atualizar quantidade do item: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def get_card_stock(self, card_id: str) -> int:
        db = Database().connect()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT stock FROM cards WHERE id = %s", (card_id,))
            result = cursor.fetchone()
            return result[0] if result else 0
        finally:
            cursor.close()
            db.close()

    def create_order_and_complete_cart(self, cart_id: int, user_id: int, total_price: float) -> None:
        db = Database().connect()
        cursor = db.cursor()
        try:
            # Criar pedido
            cursor.execute(
                "INSERT INTO orders (cart_id, user_id, total_price) VALUES (%s, %s, %s)",
                (cart_id, user_id, total_price)
            )

            # Atualizar carrinho para 'completed' (trigger já faz isso)
            cursor.execute(
                "UPDATE carts SET status = 'completed' WHERE id = %s",
                (cart_id,)
            )

            # Atualizar estoque das cartas no carrinho (trigger também faz isso)

            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception(f"Erro ao finalizar pedido: {str(e)}")
        finally:
            cursor.close()
            db.close()
