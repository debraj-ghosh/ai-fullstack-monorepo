from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.user_router import router as user_router
from app.cache.redis_client import redis_client
from app.api.auth_router import router as auth_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "FastAPI Backend is running!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/redis-health")
def redis_health():

    try:
        redis_client.ping()

        return {
            "status": "Redis Connected"
        }

    except Exception as ex:

        return {
            "status": "Redis Failed",
            "error": str(ex)
        }