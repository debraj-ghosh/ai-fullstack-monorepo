from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.schemas.common import ApiResponse
from app.services.user_service import UserService
from app.models.user import User

from app.auth.roles import (
    allow_user,
    allow_manager,
    allow_admin,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserService()


@router.post("/", response_model=ApiResponse[UserResponse])
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user : User =Depends(allow_manager),
):
    created_user = service.create_user(db, user)

    return {
        "success": True,
        "message": "User created successfully",
        "data": created_user
    }


@router.get("/", response_model=ApiResponse[list[UserResponse]])
def get_users(
    db: Session = Depends(get_db),
    current_user : User =Depends(allow_user),
):
    users = service.get_users(db)

    return {
        "success": True,
        "message": "Users fetched successfully",
        "data": users
    }


@router.get("/{user_id}", response_model=ApiResponse[UserResponse])
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user : User =Depends(allow_user),
):
    user = service.get_user_cached(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "success": True,
        "message": "Users fetched successfully",
        "data": user
    }


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user : User =Depends(allow_admin),
):
    user = service.get_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    service.delete_user(db, user)

    return {
        "success": True,
        "message": "User deleted successfully",
        "data": None
    }

@router.put("/{user_id}", response_model=ApiResponse[UserResponse])
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user : User =Depends(allow_manager),
):

    db_user = service.get_user(db, user_id)

    if not db_user:
        raise HTTPException(404, "User not found")

    user = service.update_user(db, db_user, user)
    return {
        "success": True,
        "message": "User updated successfully",
        "data": user
    }