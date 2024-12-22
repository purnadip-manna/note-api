from pydantic import BaseModel, UUID4
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserBase(BaseModel):
    email: str
    name: str


class UserView(UserBase):
    id: UUID4
    username: str
    role: RoleEnum
    is_active: bool


class UserCreate(UserBase):
    username: str
    password: str


class UserUpdatePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str