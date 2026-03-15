from api import ceremonies, ws, admin
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "ws://localhost:8000",
        "https://api.mrdegbe.com:8080",
        "wss://api.mrdegbe.com:8080",
    ],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ceremonies.router)
app.include_router(ws.router)
app.include_router(admin.router)
