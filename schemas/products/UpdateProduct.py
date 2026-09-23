from pydantic import BaseModel, EmailStr
from typing import Optional

from models.useraccount import UserRole

class UpdateProduct(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    price: Optional[str] = None
    picture: Optional[str] = None
    powerkW: Optional[float] = None
    powerkWA: Optional[float] = None
    article: Optional[str] = None
    voltage: Optional[str] = None
    categoryID: Optional[str] = None

    series: Optional[str] = None
    guarantee: Optional[str] = None
    weight:  Optional[float] = None
    noise_level: Optional[float] = None
    launch_type: Optional[str] = None
    length: Optional[int] = None    # Длина (мм)
    width: Optional[int] = None     # Ширина (мм)
    height: Optional[int] = None    # Высота (мм)
    full_description: Optional[str] = None