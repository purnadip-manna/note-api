from sqlalchemy import Column, String, Integer, Boolean
from ...database import Base


class Users(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    name: str = Column(String)
    email: str = Column(String)
    password: str = Column(String)
    is_active: bool = Column(Boolean, default=True)
    token_version: int = Column(Integer, default=1) # Handle token revocation
