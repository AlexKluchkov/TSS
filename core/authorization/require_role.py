from fastapi import Depends, HTTPException
from core.authorization.get_current_user import get_current_user
from models.useraccount import UserAccount, UserRole

def require_role(*roles: UserRole):
    def checker(
        current_user: UserAccount = Depends(get_current_user)
    ):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions",
            )

        return current_user

    return checker