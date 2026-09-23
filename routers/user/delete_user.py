from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.get_db import get_db
from models.useraccount import UserAccount, UserRole
from schemas.users.User import User
from typing import Optional

from core.authorization.require_role import require_role

router = APIRouter()

@router.delete("/delete_user/", response_model=User)
def delete_user(user_id: Optional[int] = None, email: Optional[str] = None, db: Session = Depends(get_db), user: UserAccount = Depends(require_role(UserRole.ADMIN))):
    if email is not None:
        db_user = db.query(UserAccount).filter(UserAccount.email == email).first()
    elif user_id is not None:
        db_user = db.query(UserAccount).filter(UserAccount.id == user_id).first()
    else:
        return None

    if db_user is None:
        return None

    db.delete(db_user)
    db.commit()
    return db_user