from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.ProductListRead import ProductListRead

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

category = "Дизельные высоковольтные электростанции"
description = """Высоковольтный дизель генератор мирового уровня, производится на двигателях ведущих европейских производителей – Moteurs Baudouin и Mitsubishi с высоковольтными генераторами тока на 6.3 кВ и 10.5 кВ. 
    Преимущества: 
    ● Выполняем проектные обследования объектов: определяем места установки и подключения ДЭС, проектируем прокладку кабельных линий
    ● Проектирование высоковольтных электростанций и энергокомплексов с учётом требований Постановления Правительства №87
    ● Выполняем согласование и защиту проекта в экспертизе и других контролирующих организациях
    ● Комплексное выполнение пусконаладочных и монтажных работ с проведением испытаний, наладкой РЗиА и отладкой логики работы системы
    ● Организуем комплексное обучение обслуживающего персонала заказчика
    ● Предлагаем заключить долгосрочные сервисные контракты для обеспечения бесперебойной работы
"""

@router.get("/diesel_power_plants/diesel_high-voltage_generators", response_class=HTMLResponse)
async def diesel_high_voltage_generators(request: Request, db: Session = Depends(get_db)):
    #"199344" это id Дизельные высоковольтные электростанции
    products = db.query(Offer).filter(Offer.categoryID == "199344").all()  #offset(skip).limit(limit).all()
    if not products:
        raise HTTPException(status_code=404)
        
    products_schema = [
        ProductListRead.model_validate(p)
        for p in products
    ]
    return templates.TemplateResponse(
        "list_of_products.html",
        {"request": request, "category": category, "description": description, "products": products_schema}
    )
