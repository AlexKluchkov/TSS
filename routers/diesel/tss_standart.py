from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from core.get_all_products import get_all_products

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "TSS Standart"
description = """Серия TSS Standart производится на базе линейки проверенных и надёжных двигателей марки TSS Diesel и генераторов TSS SA (технология Stamford). Высокая ремонтопригодность и простота обслуживания. Дизельные генераторы TSS Standart отпускаются по самым низким ценам и оптимальны для эксплуатации в режиме резервирования основной сети электропитания. \n 
    В зависимости от условий эксплуатации и пожелания заказчиков предлагается несколько видов исполнения серии TSS Standart: капотное, в кожухе, контейнерное и передвижное\n 
    Купить дизельный генератор серии TSS Standart можно в Москве и множестве городов России, Республики Беларусь и Республики Казахстан, в офисах официальных дилеров ГК ТСС
    """

@router.get("/diesel_power_plants/tss_standart", response_class=HTMLResponse)
async def tss_standart(request: Request):
    products = await get_all_products("180214")     #id=TSS Standart
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products}
    )
