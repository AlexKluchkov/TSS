from fastapi import APIRouter, Request, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from db.get_db import get_db
from models.offer import Offer
from schemas.ProductListRead import ProductListRead

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/search", response_class=HTMLResponse)
def search_of_product(request: Request, q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    products = db.query(Offer).filter(or_(Offer.name.ilike(f"%{q}%"), Offer.full_description.ilike(f"%{q}%"))).all()
    if not products:
        return templates.TemplateResponse(
            "search_products.html",
            {"request": request, "search": f"Найдено товаров: {len(products)}", "products": None}
        )

    products_schema = [
        ProductListRead.model_validate(p)
        for p in products
    ]

    return templates.TemplateResponse(
        "search_products.html",
        {"request": request, "search": f"Найдено товаров: {len(products)}", "products": products_schema}
    )
