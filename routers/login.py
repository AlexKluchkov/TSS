from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from db.get_db import get_db
from core.authorization.hashing_password import *
from core.authorization.jwt_token import create_access_token
from models.useraccount import UserAccount

#dsfefeffr@re.hui
#1234567890

from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = db.query(UserAccount).filter(UserAccount.email == form_data.username).first()
    print(db_user)
    print(verify_password(form_data.password, db_user.password_hash))
    if not db_user or not verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = create_access_token(db_user.id)

    response = RedirectResponse(
        url="/users/me",
        status_code=303,
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
    )
    return response