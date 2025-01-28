from fastapi import APIRouter

from app.api.v1.endpoints import auth, aws

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(aws.router, prefix="/aws", tags=["aws"])
