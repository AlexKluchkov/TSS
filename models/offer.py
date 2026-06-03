from sqlalchemy import Column, Integer, Float, String
from db.database import Base

class Offer(Base):
    __tablename__ = "Offer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String)
    price = Column(String, index=True)
    picture = Column(String, nullable=True)
    powerkW = Column(Float, nullable=True)
    powerkWA = Column(Float, nullable=True)
    article = Column(String, index=True)
    voltage = Column(String)

    series = Column(String)
    categoryID = Column(String) #id категория для поиска товаров

    guarantee = Column(String, nullable=True)
    weight = Column(Float, nullable=True)     # Вес (кг)
    noise_level = Column(Float, nullable=True) # Уровень шума (dB/7м)

    length = Column(Integer, nullable=True)    # Длина (мм)
    width = Column(Integer, nullable=True)     # Ширина (мм)
    height = Column(Integer, nullable=True)    # Высота (мм)
    #
    full_description = Column(String, nullable=True)
