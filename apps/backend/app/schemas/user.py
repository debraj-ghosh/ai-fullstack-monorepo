from enum import Enum
from pydantic import BaseModel, EmailStr, ConfigDict


class UserRole(str, Enum):
    USER = "USER"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    pass
    password: str
    role: UserRole = UserRole.USER


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)