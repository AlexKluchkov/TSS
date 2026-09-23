from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from core.authorization.get_current_user import get_current_user
from fastapi.responses import HTMLResponse
from models.useraccount import UserAccount

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/users/me", response_class=HTMLResponse)
def about_user(request: Request, current_user: UserAccount = Depends(get_current_user),):
    current_user
    return templates.TemplateResponse(
        "user_administration/about_user.html",
        {"request": request, "user": current_user}
    ) 
    