from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.ProductListRead import ProductListRead

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "TSS Prof"
description = """Серия дизельных генераторов производится с использованием двигателей марок Weichai, Yuchai, Quanchai, TSS Diesel. Высокий уровень надёжности, соответствующий мировым стандартам. Дизельный генератор этой серии универсален в плане применения и может эксплуатироваться как в режиме основного источника электроснабжения, так и в виде резервного генератора. \n 
    В зависимости от условий эксплуатации и пожелания заказчиков предлагается несколько видов исполнения серии TSS Prof: в кожухе, контейнерное и передвижное. \n
    Купить дизельный генератор серии TSS Prof можно в Москве и множестве городов России, Республики Беларусь и Республики Казахстан, в офисах официальных дилеров ГК ТСС.
"""

@router.get("/diesel_power_plants/tss_prof", response_class=HTMLResponse)
async def tss_prof(request: Request, db: Session = Depends(get_db)):
    #"180213" это id TSS Prof
    products = db.query(Offer).filter(Offer.categoryID == "180213").all()  #offset(skip).limit(limit).all()
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
