from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    #slug: Optional[str]
    powerkW: Optional[str | None]
    powerkWA: Optional[str | None]
    article: str
    voltage: str
    price: str
    picture: Optional[str]
