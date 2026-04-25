from pydantic import BaseModel
from typing import Optional

class AboutProduct(BaseModel):
    name: str
    price: float
    series: str
    powerkW: Optional[float | None]
    powerkWA: Optional[float | None]
    guarantee: Optional[str]
    weight: int
    full_description: str
    #тип горючего
    #инврьорный или нет
    #двух или четырех тактный
    #габариты
    #громкость
