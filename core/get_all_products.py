from core.parser import parser
from schemas.Product import Product

from slugify import slugify

async def get_all_products(categoryId):
    root = await parser()
    products = []
    for offer in root.xpath('//offer'):
        if((offer.xpath('categoryId/text()')[0] == categoryId) and (offer.xpath('price/text()')[0] != "0")):
            product = Product(
                name=offer.xpath('name/text()')[0] if offer.xpath('name/text()') else None,
                #slug=slugify(str(offer.xpath('name/text()')[0])),
                article = offer.xpath('.//param[@name="Артикул"]/text()')[0] if offer.xpath('.//param[@name="Артикул"]/text()') else None,
                voltage = offer.xpath('.//param[@name="Выходное напряжение (В)"]/text()')[0] if offer.xpath('.//param[@name="Выходное напряжение (В)"]/text()') else None,
                powerkW = offer.xpath('.//param[@name="Мощность номинальная, кВт"]/text()')[0] if offer.xpath('.//param[@name="Мощность номинальная, кВт"]/text()') else None,
                powerkWA = offer.xpath('.//param[@name="Мощность номинальная, кВА"]/text()')[0] if offer.xpath('.//param[@name="Мощность номинальная, кВА"]/text()') else None,
                price=float(offer.xpath('price/text()')[0]) if offer.xpath('price/text()') else None,
                picture=offer.xpath('picture/text()')[0] if offer.xpath('picture/text()') else None,
            )
            products.append(product)
    return products