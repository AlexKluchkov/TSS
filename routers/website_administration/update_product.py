from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.get_db import get_db
from core.price_formatting import price_formatting
from core.authorization.require_role import require_role
from core.authorization.hashing_password import hash_password

from models.offer import Offer
from models.useraccount import UserAccount, UserRole

from schemas.products.UpdateProduct import UpdateProduct

from slugify import slugify


router = APIRouter()


@router.patch("/products/{product_id}", response_model=UpdateProduct)
def update_product(product_id: int,data: UpdateProduct,db: Session = Depends(get_db), user: UserAccount = Depends(require_role(UserRole.SELLER))):
    product = (db.query(Offer).filter(Offer.id == product_id).first())
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Товар не найден",
        )

    if data.name is not None:
        product.name = data.name
        product.slug = slugify(data.name)

    if data.article is not None:
        product.article = data.article

    if data.voltage is not None:
        product.voltage = data.voltage

    if data.powerkW is not None:
        product.powerkW = data.powerkW

    if data.powerkWA is not None:
        product.powerkWA = data.powerkWA

    if data.price is not None:
        product.price = price_formatting(data.price)

    if data.picture is not None:
        product.picture = data.picture

    if data.categoryID is not None:
        product.categoryID = data.categoryID

    if data.series is not None:
        product.series = data.series

    if data.guarantee is not None:
        product.guarantee = data.guarantee

    if data.weight is not None:
        product.weight = data.weight

    if data.noise_level is not None:
        product.noise_level = data.noise_level

    if data.launch_type is not None:
        product.launch_type = data.launch_type

    if data.length is not None:
        product.length = data.length

    if data.width is not None:
        product.width = data.width

    if data.height is not None:
        product.height = data.height

    if data.full_description is not None:
        product.full_description = data.full_description

    db.commit()
    db.refresh(product)

    return product