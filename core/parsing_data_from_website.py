from core.parser import parser
from core.price_formatting import price_formatting
from core.xpath_validation import xpath_validation
from schemas.ProductCreate import ProductCreate

from fastapi import Depends
from sqlalchemy.orm import Session
from models.offer import Offer

from slugify import slugify

async def parsing_data_from_website(db: Session):
    root = await parser()
    categoryId = ["199344", "180034", "180212", "180213", "180214", "180215", "194682", "192425"]  # это номера категорий генераторов на сайте tss

    for offer in root.xpath('//offer'):
        if offer.xpath('categoryId/text()')[0] in categoryId and offer.xpath('price/text()')[0] != "0":
            product = ProductCreate(
                name = offer.xpath('name/text()')[0],
                slug = slugify(str(offer.xpath('name/text()')[0])),
                article = xpath_validation( offer, './/param[@name="Артикул"]/text()'),
                voltage = xpath_validation( offer, './/param[@name="Выходное напряжение (В)"]/text()'),
                powerkW = xpath_validation( offer, './/param[@name="Мощность номинальная, кВт"]/text()', float ),
                powerkWA = xpath_validation( offer, './/param[@name="Мощность номинальная, кВА"]/text()', float ),
                price = price_formatting(offer.xpath('price/text()')[0]),
                picture = xpath_validation(offer, 'picture/text()'),
                categoryID = offer.xpath('categoryId/text()')[0],

                series = xpath_validation(offer, './/param[@name="Серия"]/text()'),
                guarantee = xpath_validation(offer, './/param[@name="Гарантия, срок (мес)"]/text()'),
                weight = xpath_validation(offer, './/param[@name="Масса, кг"]/text()', float),
                noise_level = xpath_validation(offer, './/param[@name="Уровень шума (dB/7м)"]/text()', float ),
                length = xpath_validation(offer, './/param[@name="Длина (мм)"]/text()', int ),
                width = xpath_validation(offer, './/param[@name="Ширина (мм)"]/text()', int ),
                height = xpath_validation(offer, './/param[@name="Высота (мм)"]/text()', int ),
                full_description = xpath_validation(offer, './/param[@name="Детальное описание товара2"]/text()'),

                #"Тип запуска" ручной/электростартер
            )
            db_product = Offer(**product.model_dump())
            db.add(db_product)
            db.commit()
            db.refresh(db_product)
    return None
