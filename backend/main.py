from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth
from app.core.config import settings

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [{"loc": err["loc"], "msg": err["msg"], "type": err["type"]} for err in exc.errors()]
    return JSONResponse(status_code=422, content={"detail": errors})

origins = ["https://poqg.live"]
if settings.APP_ENV == "development":
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
