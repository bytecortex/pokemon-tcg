from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, EmailStr
from passlib.hash import bcrypt
import mysql.connector
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

load_dotenv()

app = FastAPI()

# INICIO TRADUÇÃO DE ERROS DE LOGIN

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    translated_errors = []

    for error in exc.errors():
        msg = error.get("msg", "")
        
        # Match parcial para mensagens comuns
        if "value is not a valid email address" in msg:
            translated_msg = "O e-mail informado não é válido."
        elif "field required" in msg:
            translated_msg = "Campo obrigatório."
        elif "value is not a valid integer" in msg:
            translated_msg = "O valor informado deve ser um número inteiro."
        elif "value is not a valid string" in msg:
            translated_msg = "O valor informado deve ser um texto (string)."
        elif "none is not an allowed value" in msg:
            translated_msg = "Este campo não pode ser nulo."
        elif "str type expected" in msg:
            translated_msg = "O valor precisa ser um texto."
        elif "type_error.email" in msg:
            translated_msg = "O e-mail informado não é válido."
        else:
            # mantém a mensagem original caso não reconheça
            translated_msg = msg

        translated_errors.append(translated_msg)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": translated_errors}
    )

# FIM TRADUÇÃO DE ERROS DE LOGIN

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
            raise HTTPException(status_code=404, detail="Não encontramos um usuário cadastrado com este e-mail")

        user_id, name, hashed_password = result

        if not bcrypt.verify(user.password, hashed_password):
            raise HTTPException(status_code=401, detail="Senha incorreta")

        return {
            "message": "Login bem sucedido",
            "user": {
                "id": user_id,
                "name": name,
                "email": user.email,
            }
        }

    except Exception as e:
        raise e

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
            raise HTTPException(status_code=400, detail="Email já registrado")

        hashed_password = bcrypt.hash(user.password)

        cursor.execute(
            "INSERT INTO usuario (nome_user, email, senha) VALUES (%s, %s, %s)",
            (user.name, user.email, hashed_password)
        )
        conn.commit()

        return {"message": "Usuário registrado com sucesso"}

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        conn.close()