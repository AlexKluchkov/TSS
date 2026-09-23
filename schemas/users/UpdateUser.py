from pydantic import BaseModel, EmailStr
from typing import Optional

from models.useraccount import UserRole

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None