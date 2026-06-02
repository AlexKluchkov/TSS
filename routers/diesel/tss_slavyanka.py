from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.ProductListRead import ProductListRead

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "ТСС Славянка"
description = """Серия производится на современном российском производстве с использованием проверенных двигателей ЯМЗ и ММЗ. Продукция зарегистрирована в реестре ГИС Минпромторга. Могут эксплуатироваться как в режиме основного источника электроснабжения, так и в виде резервного генератора, идеальны для удалённых объектов. Стоимость вырабатываемой электроэнергии находится в среднем ценовом сегменте. \n
    В зависимости от условий эксплуатации и пожелания заказчиков предлагается несколько видов исполнения серии ТСС Славянка: капотное, кожухное, контейнерное и передвижное. \n 
    Купить дизель генератор серии ТСС Славянка можно в Москве и городах России, Республики Беларусь и Казахстан, в офисах официальных дилеров ГК ТСС.
"""

@router.get("/diesel_power_plants/tss_slavyanka", response_class=HTMLResponse)
async def tss_slavyanka(request: Request, db: Session = Depends(get_db)):
    #"180215" это id TSS Slavyanka
    products = db.query(Offer).filter(Offer.categoryID == "180215").all()  #offset(skip).limit(limit).all()
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
