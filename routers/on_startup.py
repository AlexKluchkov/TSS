from core.parsing_data_from_website import parsing_data_from_website

from db.get_db import get_db

@app.on_event("startup")
async def on_startup():
    db = next(get_db())
    await parsing_data_from_website(db)