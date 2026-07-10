from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.auth.password import hash_password, verify_password
from app.auth.jwt_handler import create_access_token
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, db: Session, request: RegisterRequest):

        existing_user = self.user_repository.get_by_email(
            db,
            request.email
        )

        if existing_user:
            raise ValueError("Email already exists")

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            hashed_password=hash_password(request.password),
            role="USER",
            is_active=True,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def login(self, db: Session, request: LoginRequest):

        user = self.user_repository.get_by_email(
            db,
            request.email
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            request.password,
            user.hashed_password
        ):
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError("User account is disabled")

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role,
                "id": user.id,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }