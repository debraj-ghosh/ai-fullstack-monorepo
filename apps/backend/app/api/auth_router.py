from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)

from app.services.auth_service import AuthService

auth_service = AuthService()

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    try:
        user = auth_service.register(
            db,
            request
        )
        return {
            "message": "User Registered",
            "user_id": user.id
        }
    except ValueError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    request = LoginRequest(
        email=form_data.username,
        password=form_data.password,
    )
    try:
        return auth_service.login(
            db,
            request,
        )
    except ValueError as ex:
        raise HTTPException(
            status_code=401,
            detail=str(ex),
        )
    
@router.get("/me")
def me(
    current_user: User = Depends(get_current_user),
):

    return current_user