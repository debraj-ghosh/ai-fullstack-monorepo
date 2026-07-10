from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.auth.password import hash_password



class UserRepository:

    def create(self, db: Session, user: UserCreate):

        db_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            hashed_password=hash_password(user.password),
            role=user.role,
            is_active=True,
        )

        db.add(db_user)

        try:
            db.commit()
            db.refresh(db_user)
            return db_user

        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail="Email already exists."
            )


    def get_all(self, db: Session):
        return db.query(User).all()

    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def delete(self, db: Session, user: User):
        db.delete(user)
        db.commit()

    def update(self, db: Session, db_user: User, user: UserUpdate):

        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.email = user.email
        try:
            db.commit()
            db.refresh(db_user)
            return db_user

        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail="Email already exists."
            )
        
    def get_by_email(self, db, email: str):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )