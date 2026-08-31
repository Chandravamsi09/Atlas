from fastapi import APIRouter
from backend.app.core.config import settings

router = APIRouter()


@router.get("/healthz", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT
    }
