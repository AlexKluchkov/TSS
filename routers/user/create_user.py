from db.get_db import get_db
from core.authorization.hashing_password import hash_password
from core.authorization.require_role import require_role
from schemas.users.CreateUser import CreateUser

from fastapi import Request, APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from models.useraccount import UserAccount, UserRole

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/create_user/", response_class=HTMLResponse)
def create_user(request: Request, name: str, email: str, password: str, role: UserRole, db: Session = Depends(get_db), user: UserAccount = Depends(require_role(UserRole.ADMIN))):
    #Если в бд нет записи с таким же именем добавляем запись
    user_is_exist = db.query(UserAccount).filter(UserAccount.email == email).first()

    if user_is_exist:
        raise HTTPException(
            status_code=409,
            detail=f"Пользователь с '{email}' уже существует"
        )

    user = CreateUser(
        name = name,
        email = email,
        password_hash = hash_password(password),
        role = role,
        is_active = False
    )
    db_user = UserAccount(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return templates.TemplateResponse(
        "user_administration/create_user.html",
        {"request": request, "user": db_user}
    ) 