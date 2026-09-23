from fastapi import APIRouter, Request, Depends, HTTPException

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, selectinload
from db.get_db import get_db
from models.offer import Offer
from schemas.products.ProductListRead import ProductListRead

router = APIRouter()

templates = Jinja2Templates(directory="templates")

category = "TSS Premium"

description = """
Дизель генератор TSS Premium производится на базе
надёжных двигателей Cummins, Mitsubishi, Hyundai Doosan,
Baudouin Moteurs, FPT IVECO.
"""

@router.get("/diesel_power_plants/tss_premium",response_class=HTMLResponse)
async def tss_premium(request: Request,db: Session = Depends(get_db)):
    # Получаем Offers + изображения
    products = (db.query(Offer).options(selectinload(Offer.images)).filter(Offer.categoryID == "180212").all())

    if not products:
        raise HTTPException(
            status_code=404,
            detail="Товары не найдены"
        )

    products_schema = [
        ProductListRead.model_validate(product)
        for product in products
    ]

    return templates.TemplateResponse(
        "list_of_products.html", 
        {"request": request, "category": category, "description": description, "products": products_schema}
    )
