import uuid
import aiohttp
import os

UPLOAD_DIR = "static/products"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

async def download_image(session: aiohttp.ClientSession, picture_url: str):
        # 1) Проверяем что picture_url не пустой
        if not picture_url:
            print(f"Picture URL {picture_url}: picture отсутствует")
            return None

        # 2) создать название файла
        filename = f"{uuid.uuid4()}.jpg"
        filepath = os.path.join(
            UPLOAD_DIR,
            filename
        )
        # 3) сделать запрос на picture_url
        try:
            async with session.get(picture_url) as response:
                print("Status:", response.status)
                print("Content-Type:", response.headers.get("Content-Type"))

                response.raise_for_status()
                # 5) скачать картинку
                content = await response.read()
                with open(filepath, "wb") as f:
                    f.write(content)
                print("Saved to:", filepath)
                return filepath
        except aiohttp.ClientResponseError as e:
            print(
                f"HTTP ошибка {e.status}, "
                f"URL: {picture_url}"
            )
            return None