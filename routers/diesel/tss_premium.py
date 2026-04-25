from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from core.get_all_products import get_all_products

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "TSS Premium"
description = """Дизель генератор TSS Premium производится на базе надёжных двигателей Cummins, Mitsubishi, Hyundai Doosan, Baudouin Moteurs, FPT IVECO. Прямой конкурент ведущим мировым маркам дизельных генераторов. Имеет относительно высокую стоимость, но обеспечивают низкую стоимость вырабатываемой электроэнергии. \n
    В зависимости от условий эксплуатации и пожелания заказчиков предлагается несколько видов исполнения серии TSS Premium: капотное, кожухное, контейнерное и передвижное. \n
    Купить дизельный генератор серии TSS Standart можно в Москве и множестве городов России, Республики Беларусь и Республики Казахстан, в офисах официальных дилеров ГК ТСС"""

@router.get("/diesel_power_plants/tss_premium", response_class=HTMLResponse)
async def tss_premium(request: Request):
    products = await get_all_products("180212")     #id=TSS Premium
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products}
    )
