from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from core.get_all_products import get_all_products

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "Дизельные электростанции"
description = "Дизель генератор производится в России, на мощностях собственного производственного комплекса ГК ТСС и предназначается для решения всего спектра вопросов, связанных с обеспечением резервного и основного энергоснабжения широкого круга объектов. Дизельный генератор адаптирован к отечественному топливу и разнообразным климатическим условиям регионов нашей страны. "


@router.get("/diesel_power_plants/diesel_portable", response_class=HTMLResponse)
async def diesel_portable(request: Request):
    products = await get_all_products("180034") #id=Портативные
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products}
    )
