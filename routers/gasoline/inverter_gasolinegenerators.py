from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.ProductListRead import ProductListRead

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "Инверторные бензиновые генераторы"
description = "Инверторные бензиновые генераторы ТСС обеспечивают выработку электрического тока для качественного и стабильного питания подключенной техники, и оборудования. Компактные размеры позволяют использовать инверторные бензиновые электростанции во многих бытовых ситуациях - на даче, в походе, на рыбалке, в гараже и других местах. Бензогенераторы ТСС инверторного типа производятся с использованием только качественной компонентной базы и спроектированы для эксплуатации в Российских условиях и с ГСМ отечественных стандартов."

@router.get("/gasoline_power_plants/inverter_gasolinegenerators", response_class=HTMLResponse)
async def inverter_gasolinegenerators(request: Request, db: Session = Depends(get_db)):
    #"192425" это id Бензогенераторов инверторных
    products = db.query(Offer).filter(Offer.categoryID == "192425").all()  #offset(skip).limit(limit).all()
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
