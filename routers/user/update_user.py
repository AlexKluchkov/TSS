from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.authorization.require_role import require_role
from core.authorization.hashing_password import hash_password
from db.get_db import get_db
from models.useraccount import UserAccount, UserRole
from schemas.users.User import User
from schemas.users.UpdateUser import UpdateUser

router = APIRouter()

@router.patch("/users/{user_id}", response_model=User)
def update_user(user_id: int, data: UpdateUser, db: Session = Depends(get_db),admin: UserAccount = Depends(require_role(UserRole.ADMIN))):
    db_user = (db.query(UserAccount).filter(UserAccount.id == user_id).first())

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if data.name is not None:
        db_user.name = data.name

    if data.email is not None:
        db_user.email = data.email

    if data.password is not None:
        db_user.password_hash = hash_password(data.password)

    if data.role is not None:
        db_user.role = data.role

    if data.is_active is not None:
        db_user.is_active = data.is_active

    db.commit()
    db.refresh(db_user)

    return db_user