from pydantic import BaseModel, EmailStr
from typing import Optional
from models.useraccount import UserRole

class User(BaseModel):
    name: str
    email: EmailStr
    password_hash: str
    role: UserRole = UserRole.SELLER