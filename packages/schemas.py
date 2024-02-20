from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    content: str
    user_id: int


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class Blog(BlogBase):
    id: int


# pydantic model for User

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    id: int
    password: str
    name: str


class UserUpdate(UserBase):
    email: str
    password: str


class UserLogin(UserBase):
    password: str


class User(UserBase):
    id: int
    password: str
