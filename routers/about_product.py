from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/{product_slug}", response_class=HTMLResponse)
async def about_product(request: Request, product_slug: str):
    
    return templates.TemplateResponse(
        "about_product.html",
        {"request": request, "names": names, "prices": prices, "pictures": picture}
    )