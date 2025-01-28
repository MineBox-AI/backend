from app.api.v1.endpoints import authentication, aws
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(
    authentication.router, prefix="/auth", tags=["authentication"]
)
api_router.include_router(aws.router, prefix="/aws", tags=["aws"])
