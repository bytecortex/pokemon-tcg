from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from passlib.hash import bcrypt
import mysql.connector
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

def get_connection():
    return mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DBNAME,
    )

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str

@app.post("/login")
def login(user: UserLogin):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id_user, nome_user, senha FROM usuario WHERE email = %s", (user.email,))
        result = cursor.fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="User not found")

        user_id, name, hashed_password = result

        if not bcrypt.verify(user.password, hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect password")

        return {
            "message": "Login successful",
            "user": {
                "id": user_id,
                "name": name,
                "email": user.email,
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()

@app.post("/register")
def register(user: UserRegister):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id_user FROM usuario WHERE email = %s", (user.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = bcrypt.hash(user.password)

        cursor.execute(
            "INSERT INTO usuario (nome_user, email, senha) VALUES (%s, %s, %s)",
            (user.name, user.email, hashed_password)
        )
        conn.commit()

        return {"message": "User registered successfully"}

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()