from fastapi import APIRouter, Depends
from core.authorization.require_role import require_role
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.useraccount import UserAccount, UserRole
from schemas.users.UsersRead import UsersRead

router = APIRouter()

@router.get("/users/", response_model=list[UsersRead])
def read_all_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):  #, user: UserAccount = Depends(require_role(UserRole.ADMIN))
    return db.query(UserAccount).offset(skip).limit(limit).all()