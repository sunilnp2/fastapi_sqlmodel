from sqlmodel import SQLModel
from typing import Optional


class UserBase(SQLModel):
    email: str


class UserCreate(UserBase):
    name: str
    password: str


class UserLogin(SQLModel):
    email: str
    password: str


class User(UserBase):
    id: int
    name: str
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: Optional[str] = None


# pydantic for blog
class Blog(SQLModel):
    id: int
    title: str
    content: str
    user_id: int


