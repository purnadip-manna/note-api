from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str

class User(UserBase):
    username: str

class UserView(User):
    is_active: bool


class UserCreate(User):
    password: str

class UserUpdatePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str
