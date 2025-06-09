from mysql.connector import pooling, Error
from fastapi import HTTPException
from app.core.config import settings

class Database:
    _pool = None

    def __init__(self):
        if not Database._pool:
            try:
                Database._pool = pooling.MySQLConnectionPool(
                    pool_name="mypool",
                    pool_size=5,
                    pool_reset_session=True,
                    user=settings.DB_USER,
                    password=settings.DB_PASSWORD,
                    host=settings.DB_HOST,
                    port=settings.DB_PORT,
                    database=settings.DB_NAME
                )
            except Error as e:
                raise HTTPException(status_code=500, detail=f"Database connection pool error: {e}")

    def connect(self):
        try:
            return Database._pool.get_connection()
        except Error as e:
            raise HTTPException(status_code=500, detail=f"Failed to get connection from pool: {e}")
