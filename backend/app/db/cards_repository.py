from typing import List, Optional
from app.db.connection import Database
from mysql.connector import Error

class CardRepository:
    def get_cards(self, name: Optional[str] = None, types: Optional[str] = None, limit: int = 30) -> List[dict]:
        db = Database().connect()
        cursor = db.cursor(dictionary=True)
        try:
            query = """
                SELECT id, name, image_url_small AS small, image_url_large AS large, series, rarity, price
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
