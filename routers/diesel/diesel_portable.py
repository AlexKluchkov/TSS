from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session, selectinload
from db.get_db import get_db
from models.offer import Offer
from schemas.products.ProductListRead import ProductListRead

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "Дизельные электростанции"
description = "Дизель генератор производится в России, на мощностях собственного производственного комплекса ГК ТСС и предназначается для решения всего спектра вопросов, связанных с обеспечением резервного и основного энергоснабжения широкого круга объектов. Дизельный генератор адаптирован к отечественному топливу и разнообразным климатическим условиям регионов нашей страны. "


@router.get("/diesel_power_plants/diesel_portable", response_class=HTMLResponse)
async def diesel_portable(request: Request, db: Session = Depends(get_db)):
    #"180034" это id Портативных генераторов
    products = (db.query(Offer).options(selectinload(Offer.images)).filter(Offer.categoryID == "180034").all())

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
