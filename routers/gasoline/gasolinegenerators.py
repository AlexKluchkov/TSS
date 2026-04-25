from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from core.get_all_products import get_all_products

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "Бензогенераторы"
description = "Бензогенераторы - надёжные и проверенные временем источники электроснабжения по доступной цене. Актуальный модельный ряд спроектирован с учётом отзывов наших заказчиков из всех регионов России и соответствует их реальным потребностям. Бензиновые генераторы представлены в диапазоне мощности от 1 кВт до 17 кВт и предназначены для выработки электрического тока с напряжением 230 В и частотой 50 Гц. Также, в нашем ассортименте представлены модели трёхфазных бензогенераторов, вырабатывающих ток с напряжением 400 В, что расширяет диапазон их возможных применений."

@router.get("/gasoline_power_plants/gasolinegenerators", response_class=HTMLResponse)
async def gasolinegenerators(request: Request):
    products = await get_all_products("194682") #Бензогенераторы
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products}
    )
