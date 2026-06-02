from schemas.Product import Product
from typing import Optional

class AboutProduct(Product):
    series: str
    guarantee: Optional[str] = None
    weight:  Optional[float] = None
    noise_level: Optional[float] = None
    length: Optional[int] = None    # Длина (мм)
    width: Optional[int] = None     # Ширина (мм)
    height: Optional[int] = None    # Высота (мм)
    full_description: Optional[str] = None