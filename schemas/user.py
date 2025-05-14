from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: str
    name: str
    email: EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class Users(BaseModel):
    users: list[User]


class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Optional[User | Users] = None
