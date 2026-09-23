import uuid
import aiohttp
import asyncio
import os

from db.database import SessionLocal
from models.offer import Offer
from models.offerimage import OfferImage

UPLOAD_DIR = "static/products"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

timeout = aiohttp.ClientTimeout(
    total=40
)

# 1) Взять список Offers
# 2) Пройтись по нему
# 3) Взять picture
# 4) создать название файла
# 5) сделать запрос на picture
# 6) скачать картинку
# 7) original_url = picture, local_path = скаченная картинка

async def download_image():
    db = SessionLocal()
    try:
        # 1) Взять список Offers
        products = db.query(Offer).all()
        # 2) Пройтись по нему
        async with aiohttp.ClientSession(timeout=timeout) as session:
            for product in products:
                # 3) Взять picture_url
                picture_url = product.picture
                if not picture_url:
                    print(f"Offer {product.id}: picture отсутствует")
                    continue
                # 4) Проверяем, не скачивали ли уже
                #existing_image = (db.query(OfferImage).filter(OfferImage.offer_id == product.id).first())
                #if existing_image:
                #    print(
                #        f"Offer {product.id}: изображение уже существует"
                #    )
                #    continue

                # 5) создать название файла
                filename = f"{uuid.uuid4()}.jpg"
                filepath = os.path.join(
                    UPLOAD_DIR,
                    filename
                )
                # 5) сделать запрос на picture
                try:
                    async with session.get(picture_url) as response:
                        print("Status:", response.status)
                        print("Content-Type:", response.headers.get("Content-Type"))

                        response.raise_for_status()
                        # 6) скачать картинку
                        content = await response.read()
                        with open(filepath, "wb") as f:
                            f.write(content)

                    # 7) original_url = picture, local_path = скаченная картинка
                    print("Saved to:", filepath)

                    db_product = OfferImage(
                        offer_id=product.id,
                        original_url=picture_url,
                        local_path=filepath
                    )
                    db.add(db_product)
                except aiohttp.ClientResponseError as e:
                    print(
                        f"Offer {product.id}: "
                        f"HTTP ошибка {e.status}, "
                        f"URL: {picture_url}"
                    )
                    if e.status == 404:
                        db.delete(product)
                        db.commit()
                    continue
            db.commit()
    finally:
        db.close()


asyncio.run(download_image())