from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    email: str
    name: str


class UserView(UserBase):
    id: UUID4
    username: str
    is_active: bool


class UserCreate(UserBase):
    username: str
    password: str


class UserUpdatePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str
