from db.get_db import get_db
from core.price_formatting import price_formatting
from core.authorization.require_role import require_role
from schemas.products.ProductCreate import ProductCreate
from models.useraccount import UserAccount, UserRole

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.offer import Offer

from slugify import slugify

router = APIRouter()

@router.post("/create_product/", response_model=ProductCreate)
def create_product(name: str, price: str, article: str, voltage: str, powerkW: float, powerkWA: float, picture: str, categoryID: str, series: str, guarantee: str, weight: float, noise_level: float, launch_type: str, length: int, width: int, height: int, full_description: str, db: Session = Depends(get_db), user: UserAccount = Depends(require_role(UserRole.SELLER))):
    #Если в бд нет записи с таким же именем добавляем запись
    product_is_exist = db.query(Offer).filter(Offer.name == name).first()

    if product_is_exist:
        raise HTTPException(
            status_code=409,
            detail=f"Товар с именем '{name}' уже существует"
        )

    product = ProductCreate(
        name = name,
        slug = slugify(str(name)),
        price = price_formatting(price),
        article = article,
        voltage = voltage,
        powerkW = powerkW,
        powerkWA = powerkWA,
        picture = picture,
        categoryID = categoryID,

        series = series,
        guarantee = guarantee,
        weight = weight,
        noise_level = noise_level,
        launch_type = launch_type,
        length = length,
        width = width,
        height = height,
        full_description = full_description,
        #"Тип запуска" ручной/электростартер
    )
    db_product = Offer(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product