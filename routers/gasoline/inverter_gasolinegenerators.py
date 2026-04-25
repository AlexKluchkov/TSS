from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schemas.Product import Product
from core.get_all_products import get_all_products

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "Инверторные бензиновые генераторы"
description = "Инверторные бензиновые генераторы ТСС обеспечивают выработку электрического тока для качественного и стабильного питания подключенной техники, и оборудования. Компактные размеры позволяют использовать инверторные бензиновые электростанции во многих бытовых ситуациях - на даче, в походе, на рыбалке, в гараже и других местах. Бензогенераторы ТСС инверторного типа производятся с использованием только качественной компонентной базы и спроектированы для эксплуатации в Российских условиях и с ГСМ отечественных стандартов."

@router.get("/gasoline_power_plants/inverter_gasolinegenerators", response_class=HTMLResponse)
async def inverter_gasolinegenerators(request: Request):
    products = await get_all_products("192425") #Бензогенераторы инверторные
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products}
    )
