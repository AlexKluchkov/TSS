from schemas.Product import Product
from typing import Optional

class AboutProduct(Product):
    series: Optional[str] = None
    guarantee: Optional[str] = None
    weight:  Optional[float] = None
    noise_level: Optional[float] = None
    launch_type: Optional[str] = None
    length: Optional[int] = None    # Длина (мм)
    width: Optional[int] = None     # Ширина (мм)
    height: Optional[int] = None    # Высота (мм)
    full_description: Optional[str] = None