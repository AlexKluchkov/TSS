from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.products.Product import Product
from typing import Optional

from core.authorization.require_role import require_role
from models.useraccount import UserAccount, UserRole

router = APIRouter()

@router.delete("/delete_offer/", response_model=Product)
def delete_product(offer_id: Optional[int] = None, name: Optional[str] = None, db: Session = Depends(get_db), user: UserAccount = Depends(require_role(UserRole.SELLER))):
    if name is not None:
        db_product = db.query(Offer).filter(Offer.name == name).first()
    elif offer_id is not None:
        db_product = db.query(Offer).filter(Offer.id == offer_id).first()
    else:
        return None

    if db_product is None:
        return None

    db.delete(db_product)
    db.commit()
    return db_product