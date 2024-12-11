from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    name: str


class User(UserBase):
    is_active: bool


class UserCreate(UserBase):
    password: str
