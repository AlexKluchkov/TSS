from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/about", response_class=HTMLResponse)
async def generators(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request}
    )