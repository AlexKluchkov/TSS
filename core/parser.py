import httpx
from lxml import etree

async def parser():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.tss.ru/bitrix/catalog_export/yandex_800463.xml")
    root = etree.fromstring(response.content)
    return root
