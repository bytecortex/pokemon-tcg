from typing import List, Optional
from app.db.connection import Database
from mysql.connector import Error

class CardRepository:
    def get_cards(self, name: Optional[str] = None, types: Optional[str] = None, limit: int = 30, in_stock_only: bool = False, hyper_rare: bool = False) -> List[dict]:
        db = Database().connect()
        cursor = db.cursor(dictionary=True)
        try:
            if hyper_rare is True:
                query = """
                    SELECT id, supertype, subtypes ,name, image_url_small AS small, image_url_large AS large, series, rarity, price, stock, hp, types, flavor_text
                    FROM vw_rarest_cards
                """
            elif in_stock_only is True:
                query = """
                    SELECT id, supertype, subtypes ,name, image_url_small AS small, image_url_large AS large, series, rarity, price, stock, hp, types, flavor_text
                    FROM vw_cards_in_stock
                """
            else:
                query = """
                    SELECT id, supertype, subtypes ,name, image_url_small AS small, image_url_large AS large, series, rarity, price, stock, hp, types, flavor_text
                    FROM cards
                """

            filters = []
            params = []

            if name:
                filters.append("name LIKE %s")
                params.append(f"%{name}%")
            if types:
                filters.append("types LIKE %s")
                params.append(f"%{types}%")

            if filters:
                query += " WHERE " + " AND ".join(filters)

            query += " ORDER BY RAND() LIMIT %s"
            params.append(limit)

            cursor.execute(query, params)
            return cursor.fetchall()

        except Error as e:
            raise Exception(f"Erro ao acessar o banco de dados: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def get_card_by_id(self, card_id: str) -> Optional[dict]:
        db = Database().connect()
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT id, supertype, subtypes, name, image_url_small AS small, image_url_large AS large,
                    series, rarity, price, stock, hp, types, flavor_text
                FROM cards
                WHERE id = %s
            """, (card_id,))
            return cursor.fetchone()
        except Error as e:
            raise Exception(f"Erro ao buscar card por ID: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def update_card(self, card_id: str, stock: int, price: float):
        db = Database().connect()
        cursor = db.cursor()
        try:
            cursor.execute("""
                UPDATE cards
                SET stock = %s, price = %s
                WHERE id = %s
            """, (stock, price, card_id))
            db.commit()
        except Error as e:
            raise Exception(f"Erro ao atualizar card: {str(e)}")
        finally:
            cursor.close()
            db.close()

    def get_top_selling_cards(self) -> List[dict]:
        db = Database().connect()
        cursor = db.cursor(dictionary=True)
        try:
            query = """
                SELECT card_id, card_name, total_sold, price, total_sales
                FROM vw_top_selling_cards
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            raise Exception(f"Erro ao buscar top selling cards: {str(e)}")
        finally:
            cursor.close()
            db.close()