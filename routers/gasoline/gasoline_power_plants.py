from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/gasoline_power_plants", response_class=HTMLResponse)
async def gasoline_power_plants(request: Request):
    return templates.TemplateResponse(
        "gasoline_power_plants.html",
        {"request": request}
    )