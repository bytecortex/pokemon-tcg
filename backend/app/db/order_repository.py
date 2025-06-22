from typing import List
from app.db.connection import Database
from mysql.connector import Error

class OrderRepository:

    def get_order_history(self, user_id: int) -> List[dict]:
        try:
            db = Database().connect()
            cursor = db.cursor(dictionary=True)
            cursor.execute("CALL order_history(%s)", (user_id,))
            results = cursor.fetchall()
            return results
        except Error as e:
            raise Exception(f"Erro ao acessar o banco de dados: {str(e)}")
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if db:
                try:
                    db.close()
                except:
                    pass

    def get_cards_by_order_id(self, order_id: int) -> List[dict]:
        try:
            db = Database().connect()
            cursor = db.cursor(dictionary=True)
            cursor.execute("CALL GetCardsByOrderId(%s)", (order_id,))
            results = cursor.fetchall()
            return results
        except Error as e:
            raise Exception(f"Erro ao buscar cartas do pedido: {str(e)}")
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if db:
                try:
                    db.close()
                except:
                    pass