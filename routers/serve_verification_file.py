from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/yandex_782a12f48f737f38.html")
async def serve_verification_file():
    return FileResponse("static/yandex_782a12f48f737f38.html")