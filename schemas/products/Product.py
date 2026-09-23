from pydantic import BaseModel, ConfigDict
from typing import Optional
from schemas.products.ProductImageResponse import ProductImageResponse

class Product(BaseModel):
    name: str
    slug: Optional[str] = None
    price: str
    powerkW: Optional[float] = None
    powerkWA: Optional[float] = None
    article: str
    voltage: str
    categoryID: str

    images: list[ProductImageResponse] = []

    model_config = ConfigDict(
        from_attributes=True
    )

