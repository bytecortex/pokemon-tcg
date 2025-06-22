from app.db.connection import Database

class UserRepository:
    def __init__(self):
        self.db = Database()

    def find_by_email(self, email: str):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, name, password, role FROM users WHERE email = %s", (email,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def create_user(self, name: str, email: str, hashed_password: str):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                           (name, email, hashed_password))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def email_exists(self, email: str) -> bool:
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
            conn.close()

    def get_total_users(self) -> int:
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM users")
            (total,) = cursor.fetchone()
            return total
        finally:
            cursor.close()
            conn.close()

    def get_all_users(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, name, email, role FROM users")
            rows = cursor.fetchall()
            users = [{"id": row[0], "name": row[1], "email": row[2], "role": row[3]} for row in rows]
            return users
        finally:
            cursor.close()
            conn.close()