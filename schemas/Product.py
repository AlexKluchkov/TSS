from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    slug: Optional[str] = None
    price: str
    picture: Optional[str] = None
    powerkW: Optional[float] = None
    powerkWA: Optional[float] = None
    article: str
    voltage: str
    categoryID: str

