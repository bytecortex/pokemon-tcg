from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, EmailStr
from passlib.hash import bcrypt
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import mysql.connector.errors
from pathlib import Path
from dotenv import load_dotenv
import os


if os.getenv("APP_ENV") != "production":
    parent_dir = Path(__file__).resolve().parent.parent
    dotenv_path = parent_dir / '.env'
    load_dotenv(dotenv_path)

app = FastAPI()

# Handler customizado para erros de validação do Pydantic
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [{"loc": err["loc"], "msg": err["msg"], "type": err["type"]} for err in exc.errors()]
    return JSONResponse(
        status_code=422,
        content={"detail": errors},
    )

# CORS
origins = [
    "https://poqg.live",  # Produção
]

if os.getenv("ENV") == "development":
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)

# Database connection
def get_connection():
    try:
        conn = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except mysql.connector.Error as e:
        print(f"MySQL connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")


# Schemas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

@app.post("/login")
def login(user: LoginRequest):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, name, password FROM users WHERE email = %s", (user.email,))
        result = cursor.fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Email not found")

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

    except mysql.connector.Error as e:  
        print(f"MySQL Error: {e}")
        raise HTTPException(status_code=500, detail=f"MySQL error: {e.msg}")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Internal Error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
    finally:
        cursor.close()
        conn.close()


@app.post("/register")
def register(user: RegisterRequest):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT id FROM users WHERE email = %s", (user.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = bcrypt.hash(user.password)

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (user.name, user.email, hashed_password)
        )
        conn.commit()

        return {"message": "User successfully registered"}

    except mysql.connector.Error as e:  
        print(f"MySQL Error: {e}")
        raise HTTPException(status_code=500, detail=f"MySQL error: {e.msg}")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Internal Error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
    finally:
        cursor.close()
        conn.close()
