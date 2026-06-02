from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.offer import Offer
from schemas.AboutProductRead import AboutProductRead

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/{product_slug}", response_class=HTMLResponse)
async def about_product(request: Request, product_slug: str, db: Session = Depends(get_db)):
    product = AboutProductRead.model_validate(db.query(Offer).filter(Offer.slug == product_slug).first())
    return templates.TemplateResponse("about_product.html",{"request": request, "product": product})