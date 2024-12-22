import uuid

from sqlalchemy import Column, String, Integer, Boolean, UUID, Enum
from sqlalchemy.orm import relationship

from .schemas import RoleEnum
from ...database import Base


class Users(Base):
    __tablename__ = "users"

    id: str = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    username: str = Column(String, unique=True, index=True)
    email: str = Column(String, unique=True)
    name: str = Column(String)
    password: str = Column(String)
    role: str = Column(Enum(RoleEnum), default=RoleEnum.user)
    is_active: bool = Column(Boolean, default=True)
    token_version: int = Column(Integer, default=1) # Handle token revocation

    # notes = relationship("Notes", backref="created_by", cascade="all, delete")