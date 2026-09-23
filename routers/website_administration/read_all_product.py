from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.products.ProductListRead import ProductListRead

router = APIRouter()

@router.get("/offers/", response_model=list[ProductListRead])
def read_all_product(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(Offer).offset(skip).limit(limit).all()