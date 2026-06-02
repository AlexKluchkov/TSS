from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.ProductListRead import ProductListRead

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "Бензогенераторы"
description = "Бензогенераторы - надёжные и проверенные временем источники электроснабжения по доступной цене. Актуальный модельный ряд спроектирован с учётом отзывов наших заказчиков из всех регионов России и соответствует их реальным потребностям. Бензиновые генераторы представлены в диапазоне мощности от 1 кВт до 17 кВт и предназначены для выработки электрического тока с напряжением 230 В и частотой 50 Гц. Также, в нашем ассортименте представлены модели трёхфазных бензогенераторов, вырабатывающих ток с напряжением 400 В, что расширяет диапазон их возможных применений."

@router.get("/gasoline_power_plants/gasolinegenerators", response_class=HTMLResponse)
async def gasolinegenerators(request: Request, db: Session = Depends(get_db)):
    #"194682" это id Бензогенераторов
    products = db.query(Offer).filter(Offer.categoryID == "194682").all()  #offset(skip).limit(limit).all()
    if not products:
        raise HTTPException(status_code=404)

    products_schema = [
        ProductListRead.model_validate(p)
        for p in products
    ]
    
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products}
    )
