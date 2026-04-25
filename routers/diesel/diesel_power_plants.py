from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/diesel_power_plants", response_class=HTMLResponse)
async def diesel_power_plants(request: Request):
    return templates.TemplateResponse(
        "diesel_power_plants.html",
        {"request": request}
    )