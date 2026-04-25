from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from core.get_all_products import get_all_products

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "ТСС Славянка"
description = """Серия производится на современном российском производстве с использованием проверенных двигателей ЯМЗ и ММЗ. Продукция зарегистрирована в реестре ГИС Минпромторга. Могут эксплуатироваться как в режиме основного источника электроснабжения, так и в виде резервного генератора, идеальны для удалённых объектов. Стоимость вырабатываемой электроэнергии находится в среднем ценовом сегменте. \n
    В зависимости от условий эксплуатации и пожелания заказчиков предлагается несколько видов исполнения серии ТСС Славянка: капотное, кожухное, контейнерное и передвижное. \n 
    Купить дизель генератор серии ТСС Славянка можно в Москве и городах России, Республики Беларусь и Казахстан, в офисах официальных дилеров ГК ТСС.
"""

@router.get("/diesel_power_plants/tss_slavyanka", response_class=HTMLResponse)
async def tss_slavyanka(request: Request):
    products = await get_all_products("180215")
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products}
    )
