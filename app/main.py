# import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.config import settings
from app.utils.logger import create_log
from app.utils.middleware import TokenVerificationMiddleware
from app.utils.response import success_response


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(TokenVerificationMiddleware)
    app.include_router(api_router, prefix="/api/v1")

    return app


# ========== FAST API APPLICATION ==========
app = create_app()


# ========== HEALTH CHECK ROUTE ==========
@app.get("/health")
def health_check():
    create_log("info", "Health Check")
    return success_response("Server is Healthy")
