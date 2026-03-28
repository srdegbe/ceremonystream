from api import ceremonies, ws, admin
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "https://ceremonystream.vercel.app",
        "https://engage.mrdegbe.com"
    ],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ceremonies.router)
app.include_router(ws.router)
app.include_router(admin.router)
