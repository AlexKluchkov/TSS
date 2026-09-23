from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/logout")
async def logout():
    response = RedirectResponse(
        url="/login-page",
        status_code=303,
    )

    response.delete_cookie(
        key="access_token",
    )

    return response