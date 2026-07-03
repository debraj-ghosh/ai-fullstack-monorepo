from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def hello():
    return {
        "message": "Hello from FastAPI"
    }

class User(BaseModel):
    name: str

@app.post("/api/user")
def create_user(user: User):
    return {
        "message": f"Welcome {user.name}"
    }