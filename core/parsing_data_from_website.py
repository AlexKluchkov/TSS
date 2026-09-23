from core.parser import parser
from core.price_formatting import price_formatting
from core.xpath_validation import xpath_validation
from schemas.products.ProductCreate import ProductCreate
from core.download_image import download_image

#from fastapi import Depends
from sqlalchemy.orm import Session
from models.offer import Offer
from models.offerimage import OfferImage

from slugify import slugify
import aiohttp

timeout = aiohttp.ClientTimeout(total=40)

async def parsing_data_from_website(db: Session):
    root = await parser()
    categoryId = ["199344", "180034", "180212", "180213", "180214", "180215", "194682", "192425"]  # это номера категорий на сайте с которого парсят данные
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            for offer in root.xpath('//offer'):
                if offer.xpath('categoryId/text()')[0] in categoryId and offer.xpath('price/text()')[0] != "0":
                    #Если в бд нет записи с таким же именем добавляем запись
                    product_is_exist = db.query(Offer).filter(Offer.name == offer.xpath('name/text()')[0]).first()
                    if not product_is_exist:
                        product = Offer(
                            name = offer.xpath('name/text()')[0],
                            slug = slugify(str(offer.xpath('name/text()')[0])),
                            article = xpath_validation( offer, './/param[@name="Артикул"]/text()'),
                            voltage = xpath_validation( offer, './/param[@name="Выходное напряжение (В)"]/text()'),
                            powerkW = xpath_validation( offer, './/param[@name="Мощность номинальная, кВт"]/text()', float ),
                            powerkWA = xpath_validation( offer, './/param[@name="Мощность номинальная, кВА"]/text()', float ),
                            price = price_formatting(offer.xpath('price/text()')[0]),
                            categoryID = offer.xpath('categoryId/text()')[0],

                            series = xpath_validation(offer, './/param[@name="Серия"]/text()'),
                            guarantee = xpath_validation(offer, './/param[@name="Гарантия, срок (мес)"]/text()'),
                            weight = xpath_validation(offer, './/param[@name="Масса, кг"]/text()', float),
                            noise_level = xpath_validation(offer, './/param[@name="Уровень шума (dB/7м)"]/text()', float ),
                            launch_type = xpath_validation(offer, './/param[@name="Тип запуска"]/text()'),
                            length = xpath_validation(offer, './/param[@name="Длина (мм)"]/text()', int ),
                            width = xpath_validation(offer, './/param[@name="Ширина (мм)"]/text()', int ),
                            height = xpath_validation(offer, './/param[@name="Высота (мм)"]/text()', int ),
                            full_description = xpath_validation(offer, './/param[@name="Детальное описание товара2"]/text()'),
                        )
                        db.add(product)
                        db.flush()
                        # Далее работаем с изображением
                        picture_url = xpath_validation(offer, 'picture/text()')
                        local_path = await download_image(session, picture_url)
                        if local_path:
                            image = OfferImage(
                                offer_id=product.id,
                                original_url=picture_url,
                                local_path=local_path
                            )
                            db.add(image)
            db.commit()
        except Exception:
            db.rollback()
            raise
    return None
