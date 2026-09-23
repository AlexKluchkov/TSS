from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum, Column, Integer, Float, String, Boolean
from db.database import Base

class UserRole(str, Enum):
    ADMIN = "admin"
    SELLER = "seller"
    #CUSTOMER = "customer"

class UserAccount(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(SQLEnum(UserRole), default=UserRole.SELLER, nullable=False,)
